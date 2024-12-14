import speech_recognition as sr
import pyaudio
import json
import sys
import subprocess
import os

if __name__ == '__main__':
    from consensus import consensus_sentence
else:
    from .consensus import consensus_sentence

import Levenshtein

def median_sentence(sentences):
    num_sentences = len(sentences)
    
    # Calculate pairwise distances
    distances = [[Levenshtein.distance(sentences[i], sentences[j]) for j in range(num_sentences)] for i in range(num_sentences)]
    
    # Sum the distances for each sentence
    total_distances = [sum(distances[i]) for i in range(num_sentences)]
    
    # Find the sentence with the smallest total distance
    median_index = total_distances.index(min(total_distances))
    return sentences[median_index]

def read_houndify(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            houndify = data.get('houndify', [])
            return houndify
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return []

def read_wit(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            wit = data.get('wit', [])
            return wit
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return []

def select_device(Select=False):
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("Awailable devices:")
    print("-" * 30)

    for i in range(numdevices):
        device_info = p.get_device_info_by_index(i)

        print(f"Device {i}: {device_info['name']}")

    print("-" * 30)
    print(f"Listening on Device : {p.get_device_info_by_index(0)['name']}")

    device_index = 0
    if Select:
        device_index = int(input("Enter the index of the device to use: "))

    return device_index

def recognize_speech(device_index, duration=5):
    recognizer = sr.Recognizer()

    # List all available microphone devices
    mic_list = sr.Microphone.list_microphone_names()

    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index)

    file_path = 'certificates.json'
    houndify = read_houndify(file_path)
    wit = read_wit(file_path)

    # Print the microphone being used
    print(f"\nListening to: {mic_list[microphone.device_index]}")
  
    with sr.Microphone(device_index=device_index, sample_rate=32000) as source:

        print("Listening for {} seconds...".format(duration))
        audio = recognizer.listen(source, timeout=duration)

    google_output = ""
    houndify_output = ""
    wit_output = ""

    answers_list = list()

    try:
        google_output = recognizer.recognize_google(audio)
        print("recognize_google thinks you said: " + google_output)
        answers_list.append([google_output])
    except sr.UnknownValueError:
        print("recognize_google could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    try:
        houndify_output = recognizer.recognize_houndify(audio, client_id=houndify[0]['id'], client_key=houndify[0]['key'])
        print("recognize_houndify thinks you said: " + str(houndify_output[0]) )
        answers_list.append([str(houndify_output[0])])
    except sr.UnknownValueError:
        print("recognize_houndify could not understand audio")
    except sr.RequestError as e:
        print("Error: " + str(e))        

    try:
        wit_output = recognizer.recognize_wit(audio, key=wit[0]['key'])
        print("recognize_wit thinks you said: " + wit_output.lower().replace(",", ""))

        answers_list.append([wit_output.lower().replace(",", "")])
    except sr.UnknownValueError:
        print("recognize_wit could not understand audio")
    except sr.RequestError as e:
        print("Error: " + str(e))        

    return answers_list

def coordinate_NLP_results(Select=False):
    device_index = select_device(Select=False)

    result = recognize_speech(device_index)
    # print("no consensus: ", result)  
    print(30 * '-')

    end_result_consensus_algorithm = ' '.join(consensus_sentence(result, threshold=66))
    print("consensus agreed uppon: ", end_result_consensus_algorithm)  

    end_result_Levenshtein_distance_algorithm = median_sentence(result)[0]
    print("The median sentence is:", end_result_Levenshtein_distance_algorithm)

    print(30 * '_')

    if end_result_consensus_algorithm==end_result_Levenshtein_distance_algorithm :
        print(":) The algorithms agree upon the results")  
        return ["1", end_result_consensus_algorithm]
    else:
        print(":( The algorithms did NOT agree upon the results")  
        return ["0", end_result_Levenshtein_distance_algorithm]

if __name__ == "__main__": 
    result = coordinate_NLP_results(Select=False)
    print("result: ", result)  

    if len(sys.argv) > 1:

        if sys.argv[1].endswith(('.ahk')):
            print(f"The file '{sys.argv[1]}' ends with .ahk")

            current_script_dir = os.path.dirname(os.path.abspath(__file__)) + "\\AHK\\" + sys.argv[1]
            command = ["C:\\Program Files\\AutoHotkey\\AutoHotkey.exe", current_script_dir] + result
            subprocess.run(command)

        elif sys.argv[1].endswith(('.py')):
            print(f"The file '{sys.argv[1]}' ends with .py")

            current_script_dir = os.path.dirname(os.path.abspath(__file__)) + "\\Python\\" + sys.argv[1]
            subprocess.run(["python", current_script_dir, result[0], result[1]])

        else:
            print(f"The file '{sys.argv[1]}' does not end with .ahk or .py")

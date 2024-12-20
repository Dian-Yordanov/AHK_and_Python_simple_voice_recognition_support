import sys
import subprocess
import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window

message = sys.argv[2]

def is_half_sentence_present(sentence, text):
    # Split the sentence into words
    words = sentence.split()
    half_length = len(words) // 2

    # Get the first and second halves as full words
    first_half = ' '.join(words[:half_length])
    second_half = ' '.join(words[half_length:])

    # Check if either half is present in the text
    first_half_present = first_half in text
    second_half_present = second_half in text

    return first_half_present or second_half_present

def launch_function_matching_whole_or_part_of_hotstring(test_case, test_func, use_consensus_boolean):
    continue_boolean = False
    consensus_boolean = False
    result = is_half_sentence_present(test_case, message)
    
    if(sys.argv[1] == "1" and message == test_case):
        continue_boolean = True  
        consensus_boolean = True
        print("Condition is fully met and agreed upon") 
    elif(sys.argv[1] == "1" and result):        
        if not use_consensus_boolean:
            continue_boolean = True  
            print("Condition is agreed upon but partually met") 
    elif(sys.argv[1] == "1" and not result):        
        print("Condition is agreed upon but NOT met")         
    elif(sys.argv[1] == "0"):
        if(message == test_case or result):
            if result:
                if use_consensus_boolean:
                    print("Condition is fully met but not agreed upon")
                else:
                    consensus_boolean = True
                    continue_boolean = True
                    print("Condition is partially met but agreed upon")
        else:
            print("Condition is NOT met")            
    else:
        print("Condition is NOT met")

    if use_consensus_boolean:
        if continue_boolean and consensus_boolean:
            test_func(message, test_case)
    else:
        if continue_boolean:
            test_func(message, test_case)

def test_func(message, test_case):
    if message == test_case:
        messagebox.showinfo("Message Box Title", "condition is met exactly  " + message)
    else:
        messagebox.showinfo("Message Box Title", "condition is PARTLY met  " + message)

def test_func2(message, test_case):
    print("success")
    messagebox.showinfo("Message Box Title", "++++++++" + message + " || " + test_case)

def test_func3():
    print("ttt")

launch_function_matching_whole_or_part_of_hotstring("press space", test_func2, False)
launch_function_matching_whole_or_part_of_hotstring("press space", test_func2, True)



root.destroy()
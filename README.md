# AHK_and_Python_simple_voice_recognition_support

## In short:

This is a set of scripts are designed to provide reliable speech-to-text functionality for triggering macros in Python and AutoHotkey. They are not intended to be a standalone speech-to-text solution but are meant to be easily integrated with other macros or programs. The idea is later to integrate these into a more complete solution. 

## How to use?

There are 3 main modules: 

1. "main_SVRS.py": This is the primary script for general use and main functionality.

1. "launcher_ahk.ahk": This script launches "main_SVRS.py" with "AHK\\macro_organizer.ahk" as an argument. It's an easy launcher for AHK macros defined in "AHK\\macro_organizer.ahk", using the functionality in "main_SVRS.py" for audio macro triggering. The macros are defined locally in "AHK\\macro_organizer.ahk".

2. "launcher_python.py": This script launches "main_SVRS.py" with "Python\\macro_organizer.py" as an argument. It's an easy launcher for Python macros/functions defined in "Python\\macro_organizer.py", using the functionality in "main_SVRS.py" for audio macro triggering. The macros/functions are defined locally in "Python\\macro_organizer.py".

Working with "main_SVRS.py" :

* With one command line argument (or if the argument is a string ending with .py or .ahk), it specifies which Python or AHK script to launch, using the output of "coordinate_NLP_results".

* With one command line argument that is an integer, it defines the maximum time the function will listen for audio (default is 10 seconds).

* With two arguments: The first argument is the filename of a .py or .ahk class to launch, and the second is an integer defining the maximum time the function will listen for audio (default is 10 seconds).

## Longer version:

The main idea is to either invoke the Speech-to-Text (STT) to macro functionality using Python via terminal arguments or use the Python or AHK launchers. Once invoked, the program utilizes the SpeechRecognition library to record an audio object, which is then sent to various supported speech recognition engines/APIs: CMU Sphinx, Google Speech Recognition, Wit.ai, Microsoft Azure Speech, Houndify API, IBM Speech to Text, Snowboy Hotword Detection, TensorFlow, Vosk API, OpenAI Whisper, OpenAI Whisper API, and Groq Whisper API.

In my case, I wanted to use an odd number of engines/APIs, and from the ones I tested, recognizer.recognize_google, recognizer.recognize_houndify, and recognizer.recognize_wit were the easiest to set up, free, and worked best. Offline engines like CMU Sphinx are theoretically good, but their practical speech recognition ability is quite poor. As I will explain later, this can be somewhat improved with consensus, median, and Levenshtein distance algorithms, but I would recommend using the test set of APIs as a start.

Once the audio object is recorded and sent to the recognition engines, the results are processed by two algorithms: a consensus algorithm that checks if over 50% of the engines agree on a result, and a Levenshtein distance algorithm that calculates the median sentence. If the median sentence and the agreed result from the engines match, the trigger hotword for the macro/function invocations is assumed to be correctly received, triggering them.

If the median sentence and the consensus algorithm do not agree, another final "remedy algorithm" checks if over 50% of the hotword is still recognized by the engines. This check is done in the macro organisers for both AHK and Python, offering a choice to require either full algorithm agreement or just 50% agreement to trigger a macro/function. Depending on how the AHK/Python individual macro organisers are set up, even if just 50% of the required trigger word is recognized by 66% of the engines, it should be enough for a trigger.

## Some examples to exmplain the above: 

You define "press space" as a launcher for a Python function in "args_test_python.py". After launching "launcher_python.py", you say "press space".

* recognizer.recognize_google recognizes "press space".
* recognizer.recognize_houndify recognizes "bass space".
* recognizer.recognize_wit recognizes "press Spa".

This scenario easily satisfies both the median sentence algorithm and the consensus algorithm, concluding that the median recognized sentence is "press space". Therefore, the condition is fully met, and the function is triggered.

A more problematic example would be:

* recognizer.recognize_google recognizes "press space".
* recognizer.recognize_houndify recognizes "bass space".
* recognizer.recognize_wit recognizes "bass Spa".

In this case, the agreement would be "bass space". Unless the macro organiser function trigger is set to accept 50% condition correctness, it will not be sufficient for a trigger as the condition is not fully met. However, if 50% condition correctness is allowed, then it will trigger.

The worst case would be:

* recognizer.recognize_google recognizes "best".
* recognizer.recognize_houndify recognizes "bass Spa"
* recognizer.recognize_wit recognizes "press space".

Here, no agreement will be reached by the algorithms. The sentence trigger given to the algorithm will depend on the order of the audio engines. In a First-In-First-Out (FIFO) scenario, the trigger sentence might be "best Spa", which will always result in a condition failure.

## Ok, but why? Why use algorithms for consensus, Levenshtein distance, different audio engines, even second consensus algorithm in the launcher? Like.... this is getting too complex, no?

The main challenge is that audio recognition is inherently difficult. According to Wikipedia, "Natural language processing has its roots in the 1950s." The idea of a person speaking to a computer and the computer understanding and reacting is over 75 years old. If a problem has existed in computer science for more than three-quarters of a century, don't expect it to be easily solved or the solution to work flawlessly.

The goal of this project is to create a library where endpoints of AHK or Python scripts can be defined and triggered by specific phrases being detected. This task is significantly more complex than using simple Hotstrings like those in Autohotkey's hotsrtings triggers https://www.autohotkey.com/docs/v1/Hotstrings.htm or https://pypi.org/project/keyboard/ module in Python, due to the high likelihood of audio hotstrings being misrecognized. Issues such as poor microphone quality, mispronounced words, background noise, accents, and dialects are just a few reasons why speech recognition, even after 75+ years of research, is not perfect.

Even speech recognition products from leading companies like Google, Amazon, OpenAI, IBM, and Microsoft are not foolproof. These companies often claim their algorithms are over 95% effective in recognizing speech, which is suitable for fast speech-to-text recording and narration but not perfect. The assumption here is that the recorded speech will likely have some defects and inconsistencies. As long as just over 50% of the speech matches the target trigger hotstring, it should be sufficient. Once the hotstring is recognized, additional macro functions need to be implemented manually.

This explains the need for both AHK and Python support: AHK is ideal for small Windows-based macros, while Python is a more complex, multifunctional tool.

## Ok, but what about other Speech-To-Text solutions? 

There are three main speech actions that I find most useful for tasks software can perform:

1. Narration (Speech Recognition)
2. Macro-Triggering (Voice Commands)
3. Silent Hotword or Hotstring Invocation

Additionally, there are three key features that such software may or may not have:

1. Accurate Audio Understanding: The software should correctly, quickly, and accurately understand the recorded audio (assuming that the hardware audio recording and translation into an audio object are reliable processes perfected in the 90s, though this assumption might be somewhat flawed).

1. Effective Performance: It should perform the three speech actions mentioned above well, and the user interface **MUST** be easy to navigate.

2. This may be the most controversial but I DO NOT CARE: IT MUST BE FREE for independent non-corporate users with a reasonable limit on monthly speech actions.
 
Lets just cut the crap: when I searched for software that performs these speech actions, I was repeatedly recommended Dragon NaturallySpeaking, and boy oh boy it sucks. It sucks so much that I literally just decided if I had enough time, I would write the functionality I need and make it open-source.

When something sucks so much you just put your hands in the air and say: "fuck it i will make it myself" it must suck a lot. But it gets worse: the version I tried was 800$ bucks, I will not say how much I paid but if i did pay i would want my money back. And before you say that maybe my mic sucks: its a Behringer XM 8500 ULTRAVOICE with a Arturia MiniFuse 1 audio interface - not the best, but better than what musicians used in the 80s to record audio records still listened by people to this day. This is not even the first time I am trying to make Dragon NaturallySpeaking useful - for different uses cases on different PCs through the years I tried it 3 times. It sucks. This is the truth. It is the "best audio recognition software" according to people who recall using it in the 90s ( Maybe just maybe the fact that 20 years have passed are a good reason why I believe your information is outdated ) and also according to LLMs writting "top 10" articles-websites with the aim of reaching Googles top searches. Given the price of the software, it might not be as bad as my experience suggests, but I believe alternatives are necessary.

Of course I will be honest and tell you that "free and open source" alternatives with full functionality do somewhat exist. If we go to https://alternativeto.net/software/nuance-dragon-naturallyspeaking/ you will immediately spot that these are narration software alternatives. Ok, maybe for naration there are some alternatives, what about macro triggering and silent hotstrings? Well, this is an interesting topic: there are a few solutions here each with some advantages and disadvantages: I would like to start with https://github.com/evilC/HotVoice : Amazing program, very well made but it relies on Windows Microsoft Speech Platform Runtime https://www.microsoft.com/en-us/download/details.aspx?id=27225 for personal reason I like the approach of choosing which API to use and using multiple of them with a consensus algorithm if possible. Also I like that it features AHK as it and Python are two of the most powerful and widely used automation languages.

Other alternatives that I tried was https://lilyspeech.com/. It wasn't as accurate as I hoped, but it wasn't bad either. Same can be said about https://voiceattack.com/Default.aspx . This one was a bit annoying because it often reminded me to purchase a license, but based on its options, it likely uses the same https://pypi.org/project/SpeechRecognition/ engine as I used. I honestly like it and recommend it as a ready product that propably does what a lot of people want ( but u will have to buy a licence ). There are a few things I think could be improved, though.

I will quickly also mention https://www.joshwcomeau.com/blog/hands-free-coding/ , https://github.com/serenadeai/serenade and also like 3 different LLM-to-ahk ideas using different sets of models/agents either using ChatGPT Whisper: https://blog.devgenius.io/voice-control-your-computer-using-the-magic-of-chatgpt-8adafa012ad6 or just agents via https://www.anthropic.com/news/3-5-models-and-computer-use . 

I don't want to pay for AI agents, but I have considered generating and executing local AHK scripts. However, this would also require local LLM integration, which complicates things.

## Future goals:

There are essentially three more modules that need to be implemented, each with different levels of complexity:

1. Narration: This will be easy to implement.
1. GUI: Creating a graphical user interface to combine all the modules will also be easy.
2. Background Process: Developing a background process that listens for trigger words without being resource-intensive is a challenging task, even for big companies.
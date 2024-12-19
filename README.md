# AHK_and_Python_simple_voice_recognition_support

In short:

This is a set of scripts that aim to introduce a reliable speech-to-text for macro triggering in python and Autohotkey.  This is not meant to be a standalone solution for Speech-To-Text but its mean to be easy to use by other macros or programs. 

Longer version:

The main idea it to either invoke the STT to macro functionality by Python via terminal arguments or use the Python or AHk launchers. Once invoked, the program uses https://pypi.org/project/SpeechRecognition/ to record an audio object, which later is send to a number of its supported Speech recognition engine/API: CMU Sphinx, Google Speech Recognition, Wit.ai, Microsoft Azure Speech, Houndify API, IBM Speech to Text, Snowboy Hotword Detection, Tensorflow, Vosk API , OpenAI whisper , OpenAI Whisper API and Groq Whisper API. In my case I wanted to use an odd number of engines/api and from the ones I tested "recognizer.recognize_google", "recognizer.recognize_houndify" and "recognizer.recognize_wit" were the easiest to settup, free and best working. Offline engines like CMU Sphinx are good in theory but in practice their ability to recognise speech is really bad. As I will explain later, this can be somewhat overcomed with consensus, median and Levenshtein distance algorithms, but I will recommend not to use it. Currently at the time of writting online Speech recognitiin reigns supreme. Once the audio object is recorded and send to the recognition engines, the result is given to 2 algorithms: a consensus algorithm that compares if over 50% of the engines agree upon a mutual result and a Levenshtein distance algorithm that calculates median sentence. If the median sentence and the agreed upon result from the audio engines are the same than all next steps just assume that the trigger hotword for the macro/function invocations are correctly recieved so they trigger them. If the median sentence and the consesnsus algorithm do not agree upon a result than another final "remedy algorithm" can be used to see if over 50% of the hotword is still picked up by the audio engines and this check is done in the launchers for both AHK and Python so that a choice is given if u really want to have the full algorithm agreement in order to trigger a macro/function or just 50% is enough. Depending on how the AHK/python individual function launchers are setup, even if just 50% of the required trigger word is recognised by 66% of the audio engines, it should be enough for a trigger. 

Some examples to exmplain the above: 

You define "press space" as a launcher of a python function in "args_test_python.py", then you say "press space" after launching "launcher_python.py". 
"recognizer.recognize_google" recognises "press space", 
"recognizer.recognize_houndify" recorgnises "bass space" and 
"recognizer.recognize_wit" recognises "press Spa"
Now this would be an easy agreement for both the median sentece algorithm and the consensus algorithm that the median recognised sentence is "press space", thus the condition is met exactl and the function is triggered.

A more problematic example would be:
"recognizer.recognize_google" recognises "press space", 
"recognizer.recognize_houndify" recorgnises "bass space" and 
"recognizer.recognize_wit" recognises "bass Spa"
Because now the agreement will be "bass space" and unless the launcher function trigger is set to accept 50% condition correctness, it will not be enough for a trigger as the condition is not met. If 50% condition correctness is permited, then it will trigger. 

The worst case will be:
"recognizer.recognize_google" recognises "best", 
"recognizer.recognize_houndify" recorgnises "bass Spa" and 
"recognizer.recognize_wit" recognises "press space"
Here no agreement will be reached by the algorithsm and the sentence trigger given to the algorithm will depend on the order of which the audio engines are defined. A good estimation is that because it is FIFO the trigger sentence given is "best Spa" which will always be a condition failure. 

Ok, but why? Why use algorithms for consensus, Levenshtein distance, different audio engines, even second consensus algorithm in the launcher? Like.... this is getting too complex, no?

The base problem is that audio recognition is hard. Going to Wikipedia you will read that "Natural language processing has its roots in the 1950s" - the whole idea of a person speaking to a computer and the computer understanding what is said and reacting to it is a 75+ years old idea. If a problem exists in computer science for over 3/4 of a century do not expect for it to be easilly solved and the solution to work flawlessly. 
The end idea of this project is to be a sort of a library where endpoints of AHK or Python scripts are defined and triggered upon specific phrases being detected. This is just made infinitelly more difficult than just simple Hotstrings like https://www.autohotkey.com/docs/v1/Hotstrings.htm or https://pypi.org/project/keyboard/ because there is a very high possibility that the audio hotstring is not recognised correctly. Whether it is because of bad microphone, badly said words, background noise, accents and dialects, or the hundret6s of other reasons why it may fail, speech recognition even after 75+ years of research is not perfect. Even speech recognition products provided by big leading companies like Google, Amazon, OpenAI, IBM and Microsoft doesn't always work and usually they claim that their algorithms are 95+% effectiver in speech recognition which is fine for fast speech to text recording and narration but not perfect. What I am basically assuming is that the speech that is recorded will most likelly have some defects and inconsitencies. For as long as just over 50% of the speech matches the target trigger hotstring, it should be enough. After the hotstring is recognised, additional macro function has to implemented manually. Which also explains why AHK and Python support are needed: AHK is the language for small Windows based macros while Python is a more complex multifunctionality tool. 

Ok, but what about other Speech-To-Text solutions? 

How to use?

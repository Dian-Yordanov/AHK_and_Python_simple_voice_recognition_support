# AHK_and_Python_simple_voice_recognition_support

In short:

This is a set of scripts that aim to introduce a reliable speech-to-text for macro triggering in python and Autohotkey.  This is not meant to be a standalone solution for Speech-To-Text but its mean to be easy to use by other macros or programs. 

How to use?

There are 3 main classes: 
"main_SVRS.py" - general use and main functionality; 

launcher_ahk.ahk -> launches "main_SVRS.py" with "AHK\\macro_organizer.ahk" as argument - easy launcher for ahk macros defines in "AHK\\macro_organizer.ahk" using the functionality defined in "main_SVRS.py" for audio macro triggering. The macros are defined locally in "AHK\\macro_organizer.ahk";

launcher_python.py -> launches "main_SVRS.py" with "Python\\macro_organizer.py" as argument - easy launcher for python macros/functions defines in "Python\\macro_organizer.py" using the functionality defined in "main_SVRS.py" for audio macro triggering. The macros/functions are defined locally in "Python\\macro_organizer.py"

launching "main_SVRS.py" with 1 command line argument ( or if the argument is a string ending with .py or .ahk) defines what python or ahk script to be launched and given the output of the coordinate_NLP_results. launching "main_SVRS.py" with 1 command line argument that is an int difines how long is the maximum time the function will listen for audio ( default is 10 seconds ). Launching "main_SVRS.py" with 2 arguments: first string defines file name of a .py or .ahk class to launch and second being an int defines maximum time the function will listen for audio ( default is 10 seconds ).

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

There are 3 main speech actions that I can define to be the most useful for tasks that software can do: narration ( Speech Recognition ), macro-triggering ( Voice Commands ) and silent hotword or hotstrings invocation. There are also 3 main features that such software may or may not have: 1. correct, fast and accurate understanding of the recorded audio object ( assuming that hardware audio recording and translation into an audio object is a problem solved in the 90s (not a good assumtion but this may make us go off on a tangent, and it should mostly be done well anyway )) . 2. It has to do the 3 speech actions defined above well and the UI MUST!!! be easy enough to nagivate. 3. This may be the most controversial but I DO NOT CARE: IT MUST BE FREE for single non-corporate users with somewhat reasonable limit of montly speech actions. Lets just cut the crap: when I searched for a software that does exactly the above speech actions I was recomended multiple times Dragon NaturallySpeaking and boy oh boy it sucks. It sucks so much that I literally just decided that If i have enough time i will just write the functionality i need and open source it. When something sucks so much you just put your hands in the air and say: "fuck it i will make it myself" it must suck a lot. But it gets worse: the version I tried was 800$ bucks, I will not say how much I payd but if i did pay i would want my money back. And before you say that maybe my mic sucks: its a Behringer XM 8500 ULTRAVOICE with a Arturia MiniFuse 1 audio interface - not the best, but better than what musicians used in the 80s to record audio records still listened by people to this day. This is not even the first time I am trying to make Dragon NaturallySpeaking useful - for different uses cases on different PCs through the years I tried it 3 times. It sucks. This is the truth. It is the "best audio recognition software" according to people who recall using it in the 90s ( Maybe just maybe the fact that 20 years have passed are a good reason why I believe your information is outdated ) and also according to LLMs writting "top 10" articles-websites with the aim of reaching Googles top searches. Given the price of the software I am sure that maybe it is not as bad as my experience with it is, but I literally think that alternatives are needed. 
Of course I will be honest and tell you that "free and open source" alternatives with full functionality do not exist yet. If we go to https://alternativeto.net/software/nuance-dragon-naturallyspeaking/ you will imidiatelly spot that these are naration software alternatives. Ok, maybe for naration there are some alternatives, what about macro triggering and silent hotstrings? Well, this is an interesting topic: there are a few solutions here each with some advantages and disadvantages: I would like to start with https://github.com/evilC/HotVoice : Amazing program, very well made but it relies on Windows Microsoft Speech Platform Runtime https://www.microsoft.com/en-us/download/details.aspx?id=27225 for personal reason I like the approach of choosing which API to use and using multiple of them with a consensus algorithm if possible. Also I like that it features AHK as it and Python must be the most powerful and used automation languages. 
Other alternatives that I tried was https://lilyspeech.com/ and was not as accurate as I wanted it to be but was not bad. Same can be said about https://voiceattack.com/Default.aspx -> I think this one also was a bit annoyign because it annoys you about purchasing a licence but just by the options I can tell it probably uses the same https://pypi.org/project/SpeechRecognition/ engine as I used. I honestly like it and recommend it as a ready product that propably does what a lot of people want ( but u will have to buy a licence ). There are a few things I think that can be improved upon. I will quickly also mention https://www.joshwcomeau.com/blog/hands-free-coding/ , https://github.com/serenadeai/serenade and also like 3 different LLM-to-ahk ideas using different sat of models/agents either suign ChatGPT Whisper: https://blog.devgenius.io/voice-control-your-computer-using-the-magic-of-chatgpt-8adafa012ad6 or just agents via https://www.anthropic.com/news/3-5-models-and-computer-use . I do not want to pay for AI agents but in general I have considered local ahk script generation and execution although this also means local LLM integration which complicates stuff. 


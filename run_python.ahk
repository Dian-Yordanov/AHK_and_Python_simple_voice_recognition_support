; Define the path to the output file
outputFile = %A_ScriptDir%\python_location.txt

; Run the command to echo the string into the file
RunWait, %ComSpec% /c where python > "%outputFile%", , Hide

; Read the output from the file
FileRead, OutputVar, %outputFile%

; Split the string by spaces
array := StrSplit(OutputVar, "`n")
first_element_array = % array[1]

; Define the path to the Python executable and the script
pythonPath := % first_element_array
scriptPath = %A_ScriptDir%\Script.py

self_venv = %A_ScriptDir%\self_venv.py

venvPath = %A_ScriptDir%\venv\Scripts\activate.bat

pythonOutput2 = %A_ScriptDir%\python_output_2.txt

; Run the Python script and capture the output
RunWait, %ComSpec% /K %pythonPath% %self_venv% 
; RunWait, %ComSpec% /K %pythonPath% %self_venv% > %pythonOutput2%

; Read the output
; FileRead, OutputVar2, %pythonOutput2%

; Display the output in a message box
; MsgBox, % "Python Output: " OutputVar2

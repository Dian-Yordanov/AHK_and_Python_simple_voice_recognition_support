import sys
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window

message = sys.argv[2]

def is_half_sentence_present(sentence, text):
    # Split the sentence into two halves
    half_length = len(sentence) // 2
    first_half = sentence[:half_length]
    second_half = sentence[half_length:]

    # Check if either half is present in the text
    first_half_present = first_half in text
    second_half_present = second_half in text

    return first_half_present or second_half_present

def check_if_phrase_is_whole_or_contained(test_case, test_func, use_consensus_boolean):
    continue_boolean = False
    consensus_boolean = False
    if(sys.argv[1] == "1"):
        continue_boolean = True    
    else:
        result = is_half_sentence_present(message, test_case)    
        if result:
            continue_boolean = True
            print("Condition is met")
        else:
            print("Condition is NOT met")

    if message == test_case:
        consensus_boolean = True
        # messagebox.showinfo("Message Box Title", "condition is met exactly  " + message)
    else:
        consensus_boolean = False
        # messagebox.showinfo("Message Box Title", "condition is PARTLY met  " + message)

    if use_consensus_boolean:
        if continue_boolean and consensus_boolean:
            test_func(message, test_case)
    else:
        if continue_boolean:
            test_func(message, test_case)

    return continue_boolean

def test_func(message, test_case):
    if message == test_case:
        messagebox.showinfo("Message Box Title", "condition is met exactly  " + message)
    else:
        messagebox.showinfo("Message Box Title", "condition is PARTLY met  " + message)

def test_func2(message, test_case):
    messagebox.showinfo("Message Box Title", "++++++++" + message)

test_case = "press space"
check_if_phrase_is_whole_or_contained(test_case, test_func2, False)

root.destroy()
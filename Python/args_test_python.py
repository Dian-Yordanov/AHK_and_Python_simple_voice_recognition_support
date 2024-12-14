import sys
import tkinter as tk
from tkinter import messagebox

print("teeeeeeeest",sys.argv)

root = tk.Tk()
root.withdraw()  # Hide the main window

message = sys.argv[2]
test_case = "press space"

if message == test_case:
    messagebox.showinfo("Message Box Title", "ok " + message)
else:
    messagebox.showinfo("Message Box Title", "NOT ok " + message)

root.destroy()
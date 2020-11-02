#!python3

import tkinter as tk
from tkinter  import *

def multiply():
    x= entry1.get()
    y= entry2.get()
    Label3["text"] = int(x) * int(y)

window = tk.Tk()

entry1 = tk.Entry(width = 30,relief=SUNKEN)
label1 = tk.Label(text="x")
entry2 = tk.Entry(width = 30,relief=SUNKEN)
button1 = tk.Button(text = "=", command = multiply )
Label3 = tk.Label(width = 15,relief=SUNKEN)

entry1.pack(side = "left")
label1.pack(side = "left")
entry2.pack(side = "left")
button1.pack(side = "left")
Label3.pack(side = "left")


window.mainloop()
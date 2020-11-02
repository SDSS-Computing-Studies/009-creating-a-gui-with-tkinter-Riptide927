#!python3

import tkinter as tk
from tkinter  import *
window = tk.Tk()
window.title("Bill Gates has a nice chiken")
window.geometry("260x145")
window.resizable(0,0)

photo = PhotoImage(file = "dog.png")
label1 = tk.Label(image= photo )
label2 = tk.Label(text= "Pochacco!" )
label3 = tk.Label(text = " A cuddly littl puppy! This is from the same\n creators who brought you Keropi and Kero Kero", bg = "Cyan")

label1.place(x= 100, y=10)
label2.place(x= 180, y=30)
label3.place(x=0 ,y =110)
window.mainloop()
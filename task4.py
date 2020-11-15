import tkinter as tk
from tkinter  import *
window = tk.Tk()
window.title("Bill Gates has a nice chiken")
window.geometry()
window.resizable(0,0)

photo = PhotoImage(file = "dog.png")
label1 = tk.Label(image= photo )
label2 = tk.Label(text= "Pochacco!" )
label3 = tk.Label(text = " A cuddly littl puppy! This is from the same\n creators who brought you Keropi and Kero Kero", bg = "Cyan")

label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1,)
label3.grid(row = 1, column = 0,columnspan = 2)
window.mainloop()
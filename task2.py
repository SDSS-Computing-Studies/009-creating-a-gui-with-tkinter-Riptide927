#!python3

import tkinter as tk
from tkinter  import *

window = tk.Tk()
window.title("Peter's unlicnesed vet clinic")
photo = PhotoImage(file = "dog.png")
window.geometry("650x180")
#window.resizable(0,0)

label1 = tk.Label(image= photo )
label2= tk.Label(text= "Client Database",font=("Comic Sans MS", 14) )
button1= tk.Button(text="Search by Name",font=("Comic Sans MS", 8))
entry1= tk.Entry(width= 23)
framegrid = tk.Frame(window)
#Grid stuff
labelgrid1 = tk.Label(master = framegrid, text= "Name",font=("Comic Sans MS", 7))
labelgrid2 = tk.Label(master = framegrid, text= "Type",font=("Comic Sans MS", 7))
labelgrid3 = tk.Label(master = framegrid, text= "Breed",font=("Comic Sans MS", 7))
labelgrid4 = tk.Label(master = framegrid, text= "Owner",font=("Comic Sans MS", 7))
labelgrid5 = tk.Label(master = framegrid, text= "Birtdate",font=("Comic Sans MS", 7))
Entrygrid1 = tk.Entry(master = framegrid)
Entrygrid2 = tk.Entry(master = framegrid)
Entrygrid3 = tk.Entry(master = framegrid)
Entrygrid4 = tk.Entry(master = framegrid)
Entrygrid5 = tk.Entry(master = framegrid)


label1.pack(side= TOP, anchor = NW)
label2.place(x= 210, y=40)
button1.place(x= 325, y = 0)
entry1.place(x=430, y=5)
#Gridstuff
framegrid.pack()
labelgrid1.grid(row= 0, column = 0)
labelgrid2.grid(row= 0, column = 1)
labelgrid3.grid(row= 0, column = 2)
labelgrid4.grid(row= 0, column = 3)
labelgrid5.grid(row= 0, column = 4)
Entrygrid1.grid(row= 1, column = 0)
Entrygrid2.grid(row= 1, column = 1)
Entrygrid3.grid(row= 1, column = 2)
Entrygrid4.grid(row= 1, column = 3)
Entrygrid5.grid(row= 1, column = 4)




window.mainloop()
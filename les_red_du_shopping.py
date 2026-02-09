import tkinter as tk
from tkinter import *


def do_something():
    print("vous avez appuyez")


window = tk.Tk()
label = tk.Label(window, text="Bienvenue \nau Red du \nshopping")
label.pack()

button = tk.Button(window, text="<--", command=do_something)
button.pack()

window.mainloop()

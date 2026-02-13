import tkinter as tk
from tkinter import *

inc = 1


def affiche_photo(increment):
    if increment == 1:
        return photo1
    elif increment == 2:
        return photo2
    elif increment == 3:
        return photo3
    else:
        return photo4


def change_photo(incr):
    if incr > 0 and incr < 4:
        return incr + 1
    else:
        return 1


def do_something():
    global inc
    inc = change_photo(inc)
    lbl.config(image=affiche_photo(inc))


window = tk.Tk()
label = tk.Label(window, text="Bienvenue \nau Red du \nshopping")
label.pack()

photo1 = tk.PhotoImage(file="photos/red_sport.png")
photo2 = tk.PhotoImage(file="photos/red_princesse.png")
photo3 = tk.PhotoImage(file="photos/red_dance.png")
photo4 = tk.PhotoImage(file="photos/red_boxe.png")

lbl = tk.Label(window, image=affiche_photo(inc))
lbl.pack()

button = tk.Button(window, text="-->", command=do_something)
button.pack()

window.mainloop()

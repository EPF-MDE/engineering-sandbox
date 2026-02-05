##Base from https://www.geeksforgeeks.org/python/tkinter-application-to-switch-between-different-page-frames/

import tkinter as tk
from tkinter import ttk
from tkinter import ttk
from PIL import Image, ImageTk

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("650x1155")
        self.title("Vote for your favorite dish")
        # Background
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(
            self, text="Vote", command=lambda: controller.show_frame(Page1)
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="StartPage", command=lambda: controller.show_frame(StartPage)
        )

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()

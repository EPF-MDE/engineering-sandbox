import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



interface = 0
def change_interface(n):
    global interface
    interface = n


def reset_interface():
    change_interface(0)  


def main():
    root = tk.Tk()
    root.title("Vote for your favorite food")
    root.geometry("600x1155")

    
    img = Image.open(r"C:\Users\15691\epf-programming\python projet\engineering-sandbox\vote_interface\background.jpg")
    bg_img = ImageTk.PhotoImage(img)

    root.bg_img = bg_img  
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

    title_label = tk.Label(root, text = "Vote for your favorite food", font=("Arial", 24), fg="#94E466",bg="#130D0D")
    title_label.place(relx=0.5, y=40, anchor="center")
    title_label.lift()

    if interface == 0:
        vote_button = ttk.Button(root, text="Vote", command=change_interface(1))
        result_button = ttk.Button(root, text="Results", command=change_interface(2))
        winner_button = ttk.Button(root, text="Winner", command=change_interface(3))
        reset_button = ttk.Button(root, text="Reset", command=reset_interface)

        vote_button.pack(ipadx=5, ipady=5, expand=True)
        result_button.pack(ipadx=5, ipady=5, expand=True)
        winner_button.pack(ipadx=5, ipady=5, expand=True)
        reset_button.pack(ipadx=5, ipady=5, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()

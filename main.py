from itertools import count
import tkinter as tk
import os
from tkinter import PhotoImage, messagebox, LEFT, RIGHT, TOP

# Window setup
root = tk.Tk()
root.title("pyflash - learning made easy")
root.eval("tk::PlaceWindow . center")
root.geometry("1280x720")
iconphoto = PhotoImage(file="img/icon.png")
root.configure(bg="#6985b3")
root.iconphoto(True, iconphoto)

def addCard():
    global count
    count = 0
    nWa = tk.Toplevel()
    nWa.title("pyflash - create flashcards")
    nWa.geometry("960x540")
    nWa.configure(bg="#6985b3")

    def register():
        if len(text1.get()) == 0:
            messagebox.showerror("No word entry", "No word entry")
        elif len(text2.get()) == 0:
            messagebox.showerror("No second word entry/definition", "No second word entry/definition")
        else:
            count + 1
        tk.label.config(text=count)

    tk.Label(nWa, text="word", font=('Helvetica bold', 20)).pack(expand=True)
    tk.Entry(nWa, bd=1, font=('Helvetica bold', 20), textvariable=text2).pack(expand=True)
    tk.Label(nWa, text="word/definition", font=('Helvetica bold', 20)).pack(expand=True)
    tk.Entry(nWa, bd=1, font=('Helvetica bold', 20), textvariable=text1).pack(expand=True)
    tk.Button(nWa, text="add flashcard", font=('Helvetica bold', 20), command=register).pack(expand=True)
    tk.Label(nWa, text="flashcards added: "+count).pack(expand=True)

def viewCard():
    nWb = tk.Toplevel()
    nWb.title("pyflash - view flashcards")
    nWb.geometry("960x540")
    nWb.configure(bg="#6985b3")

def options():
    nWc = tk.Toplevel()
    nWc.title("pyflash - options")
    nWc.geometry("960x540")
    nWc.configure(bg="#6985b3")


text1 = tk.StringVar() 
text2 = tk.StringVar()

# Main window code
tk.Label(root, text="hey " + str(os.getlogin()) + ", welcome to pyflash!", font=('Helvetica bold', 40)).pack(expand=True)
tk.Button(root, text="create flashcards", width=20, height=3, font=('Helvetica bold', 20), command=addCard).pack(expand=True, side=LEFT)
tk.Button(root, text="options", width=20, height=3, font=('Helvetica bold', 20), command=options).pack(expand=True, side=RIGHT)
tk.Button(root, text="view flashcards", width=20, height=3, font=('Helvetica bold', 20), command=viewCard).pack(expand=True, side=TOP)
root.mainloop()
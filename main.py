from faulthandler import disable
import tkinter as tk
import os
from tkinter import BOTTOM, PhotoImage, StringVar, messagebox, LEFT, RIGHT, TOP
import json as serializer
import random
from pyparsing import Word

open("flashcard.txt", "w").close()

# Window setup
root = tk.Tk()
root.title("pyflash - learning made easy")
root.eval("tk::PlaceWindow . center")
root.geometry("1280x720")
iconphoto = PhotoImage(file="img/icon.png")
root.configure(bg="#6985b3")
root.iconphoto(True, iconphoto)

word = tk.StringVar()
wordg = tk.StringVar()
defi = tk.StringVar()
defig = tk.StringVar()
count = tk.IntVar()
rndo = 0
c = 0


def addCard():
    nWa = tk.Toplevel()
    nWa.title("pyflash - create flashcards")
    nWa.geometry("960x540")
    nWa.configure(bg="#6985b3")

    tk.Label(nWa, text="word", font=('Helvetica bold', 20)).pack(expand=True)
    tk.Entry(nWa, bd=1, font=('Helvetica bold', 20),
             textvariable=word).pack(expand=True)
    tk.Label(nWa, text="meaning", font=(
        'Helvetica bold', 20)).pack(expand=True)
    tk.Entry(nWa, bd=1, font=('Helvetica bold', 20),
             textvariable=defi).pack(expand=True)
    tk.Button(nWa, text="add flashcard", font=(
        'Helvetica bold', 20), command=register).pack(expand=True)
    tk.Label(nWa, text="flashcards added", font=(
        'Helvetica bold', 10)).pack(side=TOP)
    tk.Label(nWa, textvariable=count, font=(
        'Helvetica bold', 10)).pack(side=BOTTOM)


def register():
    global c
    if len(word.get()) == 0:
        messagebox.showerror("No word", "No word entry")
    elif len(str(defi.get())) == 0:
        messagebox.showerror("No meaning entry", "No meaning entry")
    else:
        count.set(count.get()+1)
        c = count.get()
        with open("flashcard.txt", "a", newline="") as f:
            serializer.dump(
                {
                    "Word": word.get(),
                    "Definition": defi.get()
                }, f
            )
            f.write("\n")


def randomizer():
    global rndo
    rndo = random.randint(0, (count.get()-1))
    print(rndo)

    with open('flashcard.txt') as g:
        bruh = g.readlines()[rndo]

    result = serializer.loads(bruh)
    wordg.set(result["Word"])
    defig.set(result["Definition"])


def viewCard():
    if c < 1:
        messagebox.showerror("No flashcard entry", "No flashcard entry")
    else:
        nWb = tk.Toplevel()
        nWb.title("pyflash - view flashcards")
        nWb.geometry("960x540")
        nWb.configure(bg="#6985b3")

        def hint():
            button1.config(state="disabled")
            tk.Label(nWb, textvariable=defig, font=(
            'Helvetica bold', 20)).pack(expand=True)
            

        tk.Label(nWb, textvariable=wordg, font=(
            'Helvetica bold', 20)).pack(expand=True)
        button1 = tk.Button(nWb, text="hint", font=(
            'Helvetica bold', 20), command=hint).pack(expand=True, side=BOTTOM)

        
        randomizer()


def options():
    nWc = tk.Toplevel()
    nWc.title("pyflash - options")
    nWc.geometry("960x540")
    nWc.configure(bg="#6985b3")


# Main window code
tk.Label(root, text="hey " + str(os.getlogin()) +
         ", welcome to pyflash!", font=('Helvetica bold', 40)).pack(expand=True)
tk.Button(root, text="create flashcards", width=20, height=3, font=(
    'Helvetica bold', 20), command=addCard).pack(expand=True, side=LEFT)
tk.Button(root, text="options", width=20, height=3, font=(
    'Helvetica bold', 20), command=options).pack(expand=True, side=RIGHT)
tk.Button(root, text="view flashcards", width=20, height=3, font=(
    'Helvetica bold', 20), command=viewCard).pack(expand=True, side=TOP)
root.mainloop()

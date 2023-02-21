import tkinter as tk
import os
from tkinter import PhotoImage, StringVar, messagebox, LEFT, RIGHT, TOP
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
c = tk.IntVar()
rndo = 0


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
    tk.Label(nWa, textvariable=c).pack(expand=True)

def register():
    if len(word.get()) == 0:
        messagebox.showerror("No word", "No word entry")
    elif len(str(defi.get())) == 0:
        messagebox.showerror("No meaning entry", "No meaning entry")
    else:
        c.set(c.get()+1)
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
    rndo = random.randint(0, (c.get()-1))
    print(rndo)


    with open('flashcard.txt') as g:
        bruh=g.readlines()[rndo]

    result = serializer.loads(bruh)
    wordg.set(print(result["Word"]))
    defig.set(print(result["Definition"]))

def viewCard():
    nWb = tk.Toplevel()
    nWb.title("pyflash - view flashcards")
    nWb.geometry("960x540")
    nWb.configure(bg="#6985b3")
    randomizer()
    tk.Label(nWb, textvariable=wordg.get(), font=('Helvetica bold', 20)).pack(expand=True)
    tk.Label(nWb, textvariable=defig.get(), font=('Helvetica bold', 20)).pack(expand=True)
    
    
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

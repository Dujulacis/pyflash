import tkinter as tk
import getpass  # iegust lietotajvardu
from tkinter import BOTTOM, PhotoImage, messagebox, LEFT, RIGHT, TOP
import json
import random
import requests

# iztira teksta dokumentu atverot programmu (nakotnes versijas to varetu izveleties lietotajs)
open("flashcard.txt", "w").close()


# Window setup
root = tk.Tk()
root.title("pyflash - learning made easy")
root.geometry("1280x720")
iconphoto = PhotoImage(file="img/icon.png")
root.configure(bg="#6985b3")
root.iconphoto(True, iconphoto)

# Variable setup
word = tk.StringVar()
wordg = tk.StringVar()
defi = tk.StringVar()
defig = tk.StringVar()
count = tk.IntVar()
rndo = 0
c = 0
removecount = 0

# Functions
def addCard():  # flashcard pievienosanas logs
    nWa = tk.Toplevel()
    nWa.title("pyflash - create flashcards")
    nWa.geometry("960x540")
    nWa.configure(bg="#6985b3")
    tk.Label(nWa, text="Guide: \n 1. Add your word \n 2. Add it's definition/meaning/translation \n 3. Create flashcard \n 4. Repeat with the next words  ",
             font=('Helvetica bold', 10), wraplength=440, justify="center", bg="white").pack(expand=True)
    tk.Label(nWa, text="word", font=('Helvetica bold', 20),
             bg="white").pack(expand=True)
    tk.Entry(nWa, bd=1, font=('Helvetica bold', 20),
             textvariable=word, bg="white").pack(expand=True)
    tk.Label(nWa, text="meaning", font=(
        'Helvetica bold', 20), bg="white").pack(expand=True)
    tk.Entry(nWa, bd=1, font=('Helvetica bold', 20),
             textvariable=defi, bg="white").pack(expand=True)
    tk.Button(nWa, text="create flashcard", font=(
        'Helvetica bold', 20), command=register, bg="white").pack(expand=True)
    tk.Label(nWa, text="flashcards added", font=(
        'Helvetica bold', 10), bg="white").pack(side=TOP)
    tk.Label(nWa, textvariable=count, font=(
        'Helvetica bold', 10), bg="white").pack()
    tk.Button(nWa, text="clear flashcards", font=(
        'Helvetica bold', 10), command=clearcard, bg="white").pack(expand=True, side=BOTTOM)


def register():  # funkcija, kas parbauda vai ir ievaditas nepieciesamas vertibas kartinam,
    # pieskaita pievienoto kartinu skaitu un pievieno tas teksta dokumenta json formata
    global c
    if len(word.get()) == 0:
        messagebox.showerror("No word", "No word entry")
    elif len(str(defi.get())) == 0:
        messagebox.showerror("No meaning entry", "No meaning entry")
    else:
        count.set(count.get()+1)
        c = count.get()
        with open("flashcard.txt", "a", newline="") as f:
            json.dump(
                {
                    "Word": word.get(),
                    "Definition": defi.get()
                }, f
            )
            f.write("\n")


def clearcard():  # nodrosina kartinu notirisanu
    global rndo, c, removecount, count
    open("flashcard.txt", "w").close()
    rndo = 0
    c = 0
    removecount = 0
    count.set(0)


def viewCard():  # kartinu apskates/macisanas logs
    if c < 1:
        # parbauda vai ir izveidota vismaz viena kartina
        messagebox.showerror("No flashcard entry", "No flashcard entry")
    else:
        nWb = tk.Toplevel()
        nWb.title("pyflash - view flashcards")
        nWb.geometry("960x540")
        nWb.configure(bg="#6985b3")
        removedlist = []  # saraksts ar lietotaja zinatajiem vardiem

        def randomizer():  # funkcija, kas izvelas nejausi izveletu vardu un skaidrojumu
            hintbutton.config(state=tk.NORMAL)
            hinttext.config(textvariable=0)
            global rndo
            global removecount
            rndo = random.randint(0, (count.get()-1))
            print(rndo)
            if rndo in removedlist:
                if removecount == (count.get()):
                    # kad lietotajs "uzvar", izvele spelet atkal vai ne
                    winmsg = messagebox.askquestion(
                        "You won!", "Try again?", icon="question")
                    if winmsg == "yes":
                        removecount = 0
                        removedlist.clear()
                    else:
                        nWb.destroy()
                        removecount = 0
                        removedlist.clear()
                else:
                    randomizer()

            with open('flashcard.txt') as g:
                # nolasa random liniju teksta dokumenta
                readline = g.readlines()[rndo]

            result = json.loads(readline)
            wordg.set(result["Word"])
            defig.set(result["Definition"])

        def hint():  # funkcija, kas parada atbildi
            hintbutton.config(state=tk.DISABLED)
            hinttext.config(textvariable=defig)

        def remover():  # funkcija, kas iznem vardu (liniju) no random
            global removecount
            hintbutton.config(state=tk.NORMAL)
            hinttext.config(textvariable=0)
            removedlist.append(rndo)
            removecount += 1
            randomizer()
        tk.Label(nWb, text="Guide: \n 1. Guess the word \n 2. If you remember it, press know, to remove it from the list. \n 3. If you don't know the meaning, you can use hint to uncover it. \n 4. Press next for unknown words. \n 5. Repeat till all words are known. \n 6. Repeat the process until you are happy with your knowledge!",  font=(
            'Helvetica bold', 10), wraplength=440, justify="center", bg="white").pack(expand=True)
        tk.Label(nWb, textvariable=wordg, font=(
            'Helvetica bold', 20), bg="white").pack(expand=True)
        hinttext = tk.Label(nWb, textvariable=0, font=(
            'Helvetica bold', 20), bg="white")
        hinttext.pack(expand=True)
        nextbutton = tk.Button(nWb, text="next", font=(
            'Helvetica bold', 20), command=randomizer, state=tk.NORMAL, bg="white")
        nextbutton.pack(expand=True, side=RIGHT)
        removebutton = tk.Button(nWb, text="know", font=(
            'Helvetica bold', 20), command=remover, state=tk.NORMAL, bg="white")
        removebutton.pack(expand=True, side=LEFT)
        hintbutton = tk.Button(nWb, text="hint", font=(
            'Helvetica bold', 20), command=hint, state=tk.NORMAL, bg="white")
        hintbutton.pack(expand=True)

        randomizer()


def options():  # opciju logs, kura lietotajs varetu mainit dazadas opcijas (nakotne)
    nWc = tk.Toplevel()
    nWc.title("pyflash - options")
    nWc.geometry("960x540")
    nWc.configure(bg="#6985b3")


def get_random_quote():  # funkcija, kas izmantojot api iegust random quote
    random_quote = requests.get("http://api.quotable.io/random").json()
    quote = random_quote["content"] + "\n\n" + "~" + random_quote["author"]
    return quote


# Main window code
tk.Label(root, text="hey " + str(getpass.getuser()) +
         ", welcome to pyflash!", font=('Helvetica bold', 40), bg="white", wraplength=1100, justify="center").pack(expand=True)
tk.Label(root, text=get_random_quote(), font=('Helvetica bold', 15, ),
         wraplength=1000, justify="center", bg="white").pack()
tk.Button(root, text="1. \n create flashcards", width=20, height=3, font=(
    'Helvetica bold', 20), command=addCard, bg="white").pack(expand=True, side=LEFT)
tk.Button(root, text="options", width=20, height=3, font=(
    'Helvetica bold', 20), command=options, bg="white").pack(expand=True, side=RIGHT)
tk.Button(root, text="2. \n view flashcards", width=20, height=3, font=(
    'Helvetica bold', 20), command=viewCard, bg="white").pack(expand=True, side=BOTTOM)
root.mainloop()

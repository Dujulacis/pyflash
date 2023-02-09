import tkinter as tk
import os
from tkinter import PhotoImage, LEFT, RIGHT, TOP

# Window setup
root = tk.Tk()
root.title("pyflash - learning made easy")
root.eval("tk::PlaceWindow . center")
root.geometry("1280x720")
iconphoto = PhotoImage(file="img/icon.png")
root.iconphoto(True, iconphoto)

def addCard():
    nWa = tk.Toplevel()
    nWa.title("Create flashcards")
    nWa.geometry("960x540")

# Main window code
tk.Label(root, text="hey " + str(os.getlogin()) + " welcome to pyflash!", font=('Helvetica bold', 20)).pack(expand=True)
tk.Button(root, text="create flashcards", width=20, height=3, font=('Helvetica bold', 20), command=addCard).pack(expand=True, side=LEFT)
tk.Button(root, text="options", width=20, height=3, font=('Helvetica bold', 20)).pack(expand=True, side=RIGHT)
tk.Button(root, text="view flashcards", width=20, height=3, font=('Helvetica bold', 20)).pack(expand=True, side=TOP)
root.mainloop()
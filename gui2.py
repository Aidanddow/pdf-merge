import tkinter as tk
from tkinter import filedialog
import gui

filename = None
path = None

def getDir():
    dir = filedialog.askdirectory()
    if dir:
        txt_dirName = tk.Label(text=str(dir))
        txt_dirName.pack()
        path = str(dir)
    return dir 

def set_fname(*args, **kwargs):
    print(f"name = {textBox.get()}")
    filename = textBox.get()
    textBox.delete(0, 'end')



window = tk.Tk()

title = tk.Label(text="PDF Merger\n")
title.pack()

btn_getPath = tk.Button(text="Choose Directory to Merge", command=getDir)
btn_getPath.pack()


fileNameDialog = tk.Label(text="Enter output filename")
fileNameDialog.pack()
textBox = tk.Entry()
textBox.bind('<Return>', set_fname)
textBox.pack()

submitFnameBTN = tk.Button(text="set name", command=set_fname)
submitFnameBTN.pack()

pathDialog = tk.Label(text="")
pathDialog.pack()

if path:
    btn_submit = tk.Button(text="Merge", command = gui.funct(path, filename))


window.mainloop()
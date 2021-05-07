import tkinter as tk
from tkinter import filedialog
import gui

filename = None
path = None

def getDir():
    global path
    dir = filedialog.askdirectory()
    if dir:
        path = str(dir)
        txt_dirName = tk.Label(text=path)
        txt_dirName.pack()
        
    return dir 

def set_fname(*args, **kwargs):
    global filename
    print(f"name = {textBox.get()}")
    filename = textBox.get()
    textBox.delete(0, 'end')



window = tk.Tk()

title = tk.Label(text="PDF Merger\n")
title.pack()


directoryFrame = tk.Frame()

btn_getPath = tk.Button(text="Choose Directory to Merge", command=getDir, master=directoryFrame)
btn_getPath.pack()

pathDialog = tk.Label(text=path, master=directoryFrame)
pathDialog.pack()

directoryFrame.pack()




fileNameDialog = tk.Label(text="Enter output filename")
fileNameDialog.pack()
textBox = tk.Entry()
textBox.bind('<Return>', set_fname)
textBox.pack()

submitFnameBTN = tk.Button(text="set name", command=set_fname)
submitFnameBTN.pack()



if path != None:
    btn_submit = tk.Button(text="Merge")
    btn_submit.pack()


window.mainloop()
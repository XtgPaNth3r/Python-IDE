from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.filedialog import *
import sys
openfile = ''
filename = ''

mask = [
    ("Text files","*.txt"),
    ("Python files","*.py *.pyw"),
    ("All files","*.*"),
    ("Rich text file", "*.rtf")]

def newFile():
    global filename
    filename = "Untitled"
    text.delete('1.0', 'end')

def compFile():
    tcode = text.get('1.0', 'end')
    f = open('code.py', "w")
    f.write(tcode)

def runFile():
    import code
    
win = Tk()
win.title('WIN IDE')
win.geometry('400x400')
font = ("ubuntu", 14)

text = Text(win, width=400, height=400, font=font)
text.pack()

menubar = Menu(win)
filemenu = Menu(menubar)

file_dropdown = Menu(menubar, font=font)

menubar.add_cascade(label="File", menu=file_dropdown)

file_dropdown.add_command(label="New File",command=newFile)
file_dropdown.add_command(label="Compile",command=compFile)
file_dropdown.add_command(label="Run Module",command=runFile)
file_dropdown.add_separator()
file_dropdown.add_command(label="Exit",command=win.quit)

win.config(menu=menubar)
win.mainloop()

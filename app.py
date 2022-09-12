import os
import tkinter as tk
from tkinter import *

root = Tk()
root.title('Egy IDLE')
root.resizable(False, False)
root.geometry('650x300')

txtBox = tk.Text(root, fg='#00cc0e', bg='#00061f', height=14, width=600)

def runCode():
    code = txtBox.get(1.0, "end")

    file = open('test.py', 'w+')

    file.write(code)
    file.close()

    print('Output:>>')
    print('=============================')
    os.system('test.py')

def saveCode():
    code = txtBox.get(1.0, "end")

    file = open('test.py', 'w+')

    file.write(code)
    file.close()


run = Button(root, text='Run', fg='white', bg='green', font=('Sans serif', 20), command=runCode)
save = Button(root, text='Save', fg='white', bg='blue', font=('Sans serif', 20),  command=saveCode)

run.place(x=570, y=0)
save.place(x=10, y=0)
txtBox.place(x = 0, y = 60)

root.mainloop()
import tkinter
import os
import webbrowser
from tkinter import messagebox as mb

quitBool = False

def scaryFile():
    with open('file.txt', 'w') as newFile:
        newFile.write('i will kill you')
    webbrowser.open_new('youareanidiot.org')

def scaryMsg():
    while quitBool == False:
        mb.askokcancel('die','dead')
        mb.askquestion('dead','dead')
        mb.askyesno('dead','dead')
        mb.askyesnocancel('dead','dead')
        mb.askretrycancel('dead','dead')
        mb.showerror('dead','dead')
        mb.showinfo('dead','die')
        mb.showwarning()('dead','dead')
        os.system('shutdown /s /t 20')

with open('warnings.txt', 'r', encoding='utf-8') as warningFile:
    warningsExtraction = warningFile.read()
    warnings = warningsExtraction.split('///')
    warningFile.close()

if __name__ == '__main__':
    firstWarn = mb.askyesno("!! SECURITY WARNING !!", warnings[0])
    if firstWarn:
        secWarn = mb.askyesno("!! LAST WARNING !!", warnings[1])
        if secWarn:
            scaryMsg()
            scaryFile()
        else:
            quit()
    else:
        quit()

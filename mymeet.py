import subprocess
import pyautogui
import time
import pandas
from datetime import datetime


def join(meetID, psswd):
    subprocess.call("C:\\Users\\Lakshaya Dilliwar\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    while True:

        join1 = pyautogui.locateOnScreen('D:\VSpython\projects\zoom\join.png')
        if join1 != None:
            pyautogui.click(join1)
            print("Rogers match found (: ")
            break
        else:
            print("Sorry sir no match found ):")
            time.sleep(1)
    while True:
        IDloc = pyautogui.locateOnScreen('D:\VSpython\projects\zoom\ID.png')
        if IDloc != None:
            pyautogui.click(IDloc)
            print("Rogers 2nd step match found (: ")
            pyautogui.typewrite(meetID)
            pyautogui.click(pyautogui.locateOnScreen('D:\VSpython\projects\zoom\JB.png'))
            break
        else:
            print("Sorry sir no match found for 2nd step ):")
            time.sleep(1)
    while True:
        pswd = pyautogui.locateOnScreen('D:\VSpython\projects\zoom\psswd.png')
        if pswd != None:
            pyautogui.click(pswd)
            print("Rogers 3rd step match found (: ")
            pyautogui.typewrite(psswd)
            pyautogui.click(pyautogui.locateOnScreen('D:\VSpython\projects\zoom\psswdjoin.png'))
            break
        else:
            print("Sorry sir no match found for 3rd step ):")
            time.sleep(1)
    while True:
        Withoutvideo = pyautogui.locateOnScreen('D:\VSpython\projects\zoom\joinwithoutvideo.png')
        if Withoutvideo != None:
            pyautogui.click(Withoutvideo)
            print("Rogers 4th step match found (: ")
            break
        else:
            print("Sorry sir no match found for 4th step ):")
            time.sleep(1)
    
join("82697562431","d5Z0EM")
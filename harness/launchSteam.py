import pyautogui as pgui
import time

def run(appname, key):
    
    familybuttonRBG = (151, 187, 105)
    familybuttonPosX = 1473
    familybuttonPosy = 18

    familyinputPosX = 928
    familyinputPosY = 533

    pgui.press('win')
    time.sleep(1)
    pgui.write(appname)
    time.sleep(1)
    pgui.press('enter')
    pgui.moveTo(familybuttonPosX, familybuttonPosy)
    while True:
        if pgui.pixelMatchesColor(familybuttonPosX, familybuttonPosy, familybuttonRBG):
            print("color matched")
            break
        else:
            time.sleep(2)
    time.sleep(2)
    pgui.click()
    time.sleep(2)
    pgui.click(familyinputPosX, familyinputPosY)
    pgui.write(key)
    pgui.press('enter')

    
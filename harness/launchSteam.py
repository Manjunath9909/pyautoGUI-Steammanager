import pyautogui as pgui
import time
from . import essentials
from harness.essentials import position

def run(appname, key):
    if not essentials.isRunning(appname + ".exe"):
        familybuttonRBG = (151, 187, 105)
        familybuttonPos = position(1473, 18)
        familyinputPos = position(928, 533)

        pgui.press('win')
        time.sleep(1)
        pgui.write(appname)
        time.sleep(1)
        pgui.press('enter')
        pgui.moveTo(familybuttonPos.x, familybuttonPos.y)
        while True:
            if pgui.pixelMatchesColor(familybuttonPos.x, familybuttonPos.y, familybuttonRBG):
                break
            else:
                time.sleep(2)
        time.sleep(1)
        pgui.click()
        time.sleep(2)
        pgui.click(familyinputPos.x, familyinputPos.y)
        pgui.write(key)
        pgui.press('enter')
    else:
        print("Steam is already running")

    
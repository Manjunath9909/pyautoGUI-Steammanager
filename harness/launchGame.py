import pyautogui as pgui
import time
from . import essentials
from harness.essentials import position

def run(gameName):

    if not essentials.isRunning(gameName): 
        steamSearchBarPos = position(174, 178)
        steamSearchedFirstGamePos = position(204, 251)
        steamPlayButtonPos = position(582, 433)
        foundGameRBG = (88, 111, 150)
        gameInstalled = (65, 194, 55)
        
        pgui.press('win')
        pgui.write('steam')
        pgui.press('enter')
        time.sleep(2)
        
        pgui.move(steamSearchBarPos.x, steamSearchBarPos.y)
        pgui.click()
        pgui.write(gameName.lower())
        
        pgui.move(steamSearchedFirstGamePos.x, steamSearchedFirstGamePos.y)
        while True:
            if pgui.pixelMatchesColor(steamSearchedFirstGamePos.x, steamSearchedFirstGamePos.y, foundGameRBG):
                break
            else:
                print("Game does not exist")
                return
        pgui.click()
        pgui.move(steamPlayButtonPos.x, steamPlayButtonPos.y)
        if pgui.pixelMatchesColor(steamPlayButtonPos.x, steamPlayButtonPos.y, gameInstalled):
            pgui.click()
        else:
            print("Game not installed on steam!")
            exit(0)
    else:
        print("Game is already running!")
        exit(0)
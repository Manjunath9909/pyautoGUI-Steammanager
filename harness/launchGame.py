import pyautogui as pgui
import time
from . import essentials
from harness.essentials import position

def run(gameName):

    if not essentials.isRunning(gameName): 
        steamSearchBarPos = position(174, 178)
        steamSearchedFirstGamePos = position(204, 251)
        steamPlayButtonPos = position(582, 433)
        foundGameRBG = (50, 58, 75)
        gameInstalled = (65, 194, 55)
        
        pgui.press('win')
        pgui.write('steam')
        pgui.press('enter')
        time.sleep(3)
        
        pgui.moveTo(steamSearchBarPos.x, steamSearchBarPos.y)
        
        print(pgui.position())
        pgui.click()
        pgui.hotkey('ctrl', 'a')
        pgui.press('backspace')
        pgui.write(gameName)
        
        pgui.moveTo(steamSearchedFirstGamePos.x, steamSearchedFirstGamePos.y)
        pgui.moveTo(steamSearchedFirstGamePos.x + 5, steamSearchedFirstGamePos.y)
        if pgui.pixelMatchesColor(steamSearchedFirstGamePos.x, steamSearchedFirstGamePos.y, foundGameRBG):
            print("Game found", end="\r", flush=True)
        else:
            print("Game does not exist")
            return
        
        pgui.click()
        pgui.moveTo(steamPlayButtonPos.x, steamPlayButtonPos.y)
        if pgui.pixelMatchesColor(steamPlayButtonPos.x, steamPlayButtonPos.y, gameInstalled, tolerance=30):
            
            pgui.click()
        else:
            print("Game not installed on steam!", end="\r", flush=True)
            exit(0)
    else:
        print("Game is already running!")
        exit(0)
import pyautogui as pgui
import time
def run(appname):
    pgui.press('win')
    time.sleep(1)
    pgui.write(appname)
    time.sleep(1)
    pgui.press('enter')
    return
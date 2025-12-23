import time 
import sys
import pyautogui as pgui
from harness import launchApp, launchWarframe, launchSteam

def runapp(app):
    launchApp.run()
    return 

def rungame(gamename):
    launchWarframe.run()
    return

def launchSteam():
    launchSteam.run()
    return

#main
command = sys.argv[1]
if command == "runapp":
    runapp(sys.argv[2])
elif command == "rungame":
    rungame(sys.argv[2])
elif command == "launchsteam":
    launchSteam(sys.argv[2], sys.argv[3])
else:
    print("Shutting down")
    exit(0)
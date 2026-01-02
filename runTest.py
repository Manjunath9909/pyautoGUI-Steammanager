import time 
import sys
import  pyautogui as pgui
from harness import launchApp, launchGame, launchSteam

def runapp(app):
    launchApp.run(app)
    return 

def rungame(gamename):
    launchGame.run(gamename)
    return

def launchSteamLauncher(key):
    launchSteam.run("Steam", key)
    return

def printHelpText():
    print(

    """    
    How to use: 
        
    python runTest.py runapp <appname>  -  to launch an app of your choice")
    python runTest.py runsteam <steam family key>  -  to launch Steam app")
    python runTest.py rungame <gamename>  -  to run a Steam game"""

)
    exit(0)

#main
try:
    command = sys.argv[1]
except:
    printHelpText()

if command == "runapp":
    runapp(sys.argv[2])
elif command == "rungame":
    rungame(sys.argv[2])
elif command == "runsteam":
    launchSteamLauncher(sys.argv[2])
elif command == "-h" or command == "help":
    printHelpText()
else:
    print("displaying mouse stuff")
    pgui.displayMousePosition()
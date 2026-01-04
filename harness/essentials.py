import psutil

class position:
    x = 0
    y = 0

    def __init__(this, posx, posy):
        this.x = posx
        this.y = posy

def isRunning(processName):
    for process in psutil.process_iter(['name']):
        if process.info['name'].lower() == processName.lower():
            return True
        else:
            return False
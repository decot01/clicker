import mouse
import time
import keyboard
isclicking = False

def startclicker():
    global isclicking
    isclicking = not isclicking

keyboard.add_hotkey("F6",startclicker)

while True :
    if isclicking:
        mouse.click(button="left")
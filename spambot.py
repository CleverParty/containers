import requests
import discord
import asyncio
from config import *
import sys
import asyncio
import pyautogui
from bs4 import BeautifulSoup

print('Press Ctrl-C to quit.')
try:
    while True:
        # x, y = pyautogui.position()
        if(pyautogui.onScreen(614, 783)):
            pyautogui.screenshot('foo.png')
            pyautogui.click(x=614, y=782, clicks = 2, interval=1 , button='left')
            # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            # print("position is :={}".format(positionStr))
            # test command pyautogui.prompt('This lets the user type in a string and press OK.')
            text = "test here"
            pyautogui.typewrite(text, 1)
            pyautogui.press('enter')
        pyautogui.screenshot('foo.png')
        pyautogui.click(x=614, y=782, clicks = 2, interval=1 , button='left')
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print("position is :={}".format(positionStr))
        # test command pyautogui.prompt('This lets the user type in a string and press OK.')
        text = "test here"
        pyautogui.typewrite(text, 1)
        pyautogui.press('enter')

except KeyboardInterrupt:
     print('\nDone.')

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
client = discord.Client()
token = sys.argv[1]
text = "test here"
# text field input 
pyautogui.typewrite(text, 1)
# clicks function
# pag.click(x, y, clicks, interval, button)
# clicks key
pyautogui.press('enter')

# Get and print the mouse coordinates.

# permision integer - discord = 1811950599

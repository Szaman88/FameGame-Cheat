#Created by XNizi // https://github.com/xnizi

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05) #How fast the program will run | best setting in my opinion 0.05
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(x, y)[0] == 0: # - left glove coordinates {color} || [0] == 0 ([R] ~ color in RGB) <-- if the script detects a color at the given coordinates program clicks
        click(x, y) # - Here Script make Click (left glove)
    if pyautogui.pixel(x, y)[0] == 0: # - right glove coordinates {color} ||
        click(x, y) # - Here Script make Click (right glove)
    
   

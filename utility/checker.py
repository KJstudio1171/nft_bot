import pyautogui as p
from PIL import ImageGrab
import time as t
import keyboard

screen = ImageGrab.grab()

def printSleep(position,time):
	print(position)
	t.sleep(time)
keyboard.add_hotkey('p',lambda:printSleep((p.position().x,p.position().y),0.1))
keyboard.add_hotkey('c',lambda:printSleep(screen.getpixel(p.position()),0.1))
keyboard.wait('e')
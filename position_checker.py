import pyautogui as p
import keyboard
import time

while True:
	if keyboard.is_pressed('t'):
		time.sleep(0.5)
		print(p.position())
	if keyboard.is_pressed('e'):
		quit()

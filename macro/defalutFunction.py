import pyautogui as p
import time as t

def click_wait(nft_position,wait_time):
	p.moveTo(nft_position)
	p.click(nft_position)
	t.sleep(wait_time)

def copy(position,wait_time):
	p.moveTo(position)
	p.click(position)
	t.sleep(wait_time)
	p.click(position)
	p.hotkey('ctrl','c')
	t.sleep(1)
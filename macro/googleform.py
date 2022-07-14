import pyautogui as p
import time as t
import defalutFunction as df
import keyboard

g_form = 'https://forms.gle/aae8cahYThQ5U8728'

discord = [(1652, 221),(1661, 244),(1656, 270)]
twitter = [(1373, 219),(1377, 241),(1380, 267)]
wallet = [(2414, 220),(2410, 244),(2412, 272)]

g_addurl = (273, 28)
g_url = (1021, 60)
g_discord = (401, 184)
g_twitter = (426, 361)
g_answer = (346, 587)
g_wallet = (410, 853)
g_confirm = (356, 935)
g_delete = (474, 27)

keyboard.add_hotkey('e',lambda:quit())

for _ in range(17):
	for i in range(3):
		df.click_wait(g_addurl,1)
		df.click_wait(g_url,1)
		keyboard.write(g_form)
		t.sleep(1)
		keyboard.press('enter')
		t.sleep(2)
		p.click(1151, 710)
		p.scroll(-1500)
		df.copy(discord[i],1)
		df.click_wait(g_discord,1)
		p.hotkey('ctrl','v')
		df.copy(twitter[i],1)
		df.click_wait(g_twitter,1)
		p.hotkey('ctrl','v')
		df.click_wait(g_answer,1)
		df.copy(wallet[i],1)
		df.click_wait(g_wallet,1)
		p.hotkey('ctrl','v')
		df.click_wait(g_confirm,1)
		df.click_wait(g_delete,1)
	p.click(discord[0])
	p.scroll(-200)
	p.click(1150,750)
	

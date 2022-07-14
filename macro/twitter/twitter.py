import pyautogui as p
import time as t
import keyboard as k
import random as r
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import defalutFunction as df

task_url = 'https://twitter.com/TheSphynxUS/status/1526250071272181761'
is_followed = False

position_list = []
follow = (0, 0)
retweet = (0, 0)
like = (0, 0)
reply = (0, 0)
finish = (1600,-3820)

f_url = (1074, -3774)
f_container_list_start = (1531, -3777)
f_container_list = [(1089, -3454),(1093, -3550),(1095, -3495),(1093, -3594),(1098, -3644)]
f_container_start = (500, -3820)
f_container_gap = 100
f_finish = (1609, -3820)

f = open('tag.txt','r')
taglist = f.readlines()

k.add_hotkey('i',lambda:init_program(5))
k.add_hotkey('t',lambda:truefollow())
k.add_hotkey('p',lambda:position_list.append((p.position().x,p.position().y)))
k.add_hotkey('f',lambda:firefox_twitter_macro())
k.add_hotkey('s',lambda:twitter_macro(5,92,True))

def firefox_twitter_macro():
	for i in range(5):
		df.click_wait(f_container_list_start, 1 + r.random())
		df.click_wait(f_container_list[i],2 + r.random())
		firefox_twitter_macro_sub()

def firefox_twitter_macro_sub():
	global follow,retweet,like,reply
	position = (0, 0)
	follow = position_list[0]
	retweet = position_list[1]
	like = position_list[2]
	reply = position_list[3]
	for i in range(10):
		position = (f_container_start[0] + i * f_container_gap, f_container_start[1])
		df.click_wait(position,1 + r.random())
		t.sleep(2+r.random())
		df.click_wait(f_url,1 + r.random())
		k.write(task_url)
		k.write('\n')
		t.sleep(4.5+r.random())
		if not is_followed:
			df.click_wait(follow,2+r.random())
		df.click_wait(retweet,1+r.random())
		df.click_wait(retweet,1+r.random())
		df.click_wait(like,1+r.random())
		df.click_wait(reply,1+r.random())
		r.shuffle(taglist)
		k.write(taglist[0].replace('\n',' ') + taglist[1].replace('\n',' ') + taglist[2].replace('\n',''))
		p.hotkey('ctrl','enter')
		t.sleep(2.3+r.random())
	df.click_wait(f_finish,1 + r.random())

def twitter_macro(start,end,mode):
	global follow,retweet,like,reply
	follow = position_list[0]
	retweet = position_list[1]
	like = position_list[2]
	reply = position_list[3]
	for i in range(start,end):
		os.chdir('C:\\Users\\june1\\Desktop\\암호화폐\크롬')
		os.system('계정' + str(i) + '.lnk')
		t.sleep(2+r.random())
		k.write(task_url)
		k.write('\n')
		t.sleep(4.5+r.random())
		if not is_followed:
			df.click_wait(follow,2+r.random())
		df.click_wait(retweet,1+r.random())
		df.click_wait(retweet,1+r.random())
		df.click_wait(like,1+r.random())
		df.click_wait(reply,1+r.random())
		r.shuffle(taglist)
		k.write(taglist[0].replace('\n',' ') + taglist[1].replace('\n',' ') + taglist[2].replace('\n',''))
		p.hotkey('ctrl','enter')
		t.sleep(2.3+r.random())
		if mode :
			df.click_wait(finish,1)
			t.sleep(2)

def init_program(start):
	os.chdir('C:\\Users\\june1\\Desktop\\암호화폐\크롬')
	os.system('계정' + str(start) + '.lnk')
	t.sleep(2+r.random())
	k.write(task_url)
	k.write('\n')
	t.sleep(3.5+r.random())
	


def truefollow():
	global is_followed
	is_followed = True

k.wait('e')
f.close()

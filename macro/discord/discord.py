import pyautogui as p
import time as t
import random as r
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import defalutFunction as df
import keyboard

times = 5

firefoxPosition1 = [(1364, 22), (1472, 23), (1573, 21) ,(1677, 23), (1783, 22), (1875, 22), (1985, 22), (2089, 18), (2179, 23) ,(2284, 19)]
firefoxPosition2 = [(74, 25), (189, 24), (297, 24), (399, 22), (505, 21), (605, 21) ,(700, 20), (793, 23), (891, 23), (999, 26)]
chromePosition = [(578, -3607), (1037, -3607), (1511, -3607), (600, -2986), (1070, -3015), (1487, -2991), (648, -2449), (1012, -2495), (1416, -2491), (714, -1954), (1173, -1954),(1507, -1954)]
#(2288, 307), (2280, 772), (1590, 709), (1622, 268), (972, 215), (933, 784), (200, 803)]
f = open('finish','r')
chattingList = f.readlines()
# first = open('first.txt','r',encoding="UTF-8")
# korean = open('koreanlist.txt','r',encoding="UTF-8")
# last = open('last.txt','r',encoding="UTF-8")
# firstList = first.readlines()
# koreanList = korean.readlines()
# lastList = last.readlines()
# chattingList = []
# for i in koreanList:
# 	for j in lastList:
# 		chattingList.append(i.strip().replace('\n','') + j)
# for i in koreanList:
# 	for j in lastList:
# 		key = r.random()
# 		if key > 0.9:
# 			chattingList.append(firstList[r.randint(0,len(firstList)-1)].strip().replace('\n','')+i.strip().replace('\n','')+j)



# for i in range(times):
# 	startTime = t.time()
# 	for j in firefoxPosition1:
# 		df.click_wait(j,0.4 + r.random()/2)
# 		keyboard.write(chattingList[r.randint(0,len(chattingList) - 1)],0.2 + r.random()/3)
# 	for k in firefoxPosition2:
# 		df.click_wait(k,0.4 + r.random()/2)
# 		keyboard.write(chattingList[r.randint(0,len(chattingList) - 1)],0.2 + r.random()/3)
# 	endTime = t.time()
# 	if (endTime - startTime < 61):
# 		t.sleep(61 - ( endTime - startTime ))

count = 820

for i in range(times):
	startTime = t.time()
	for j in chromePosition:
		df.click_wait(j,0.4 + r.random()/2)
		keyboard.write(chattingList[count],0.2 + r.random()/3)
		keyboard.write('\n')
		count += 1
	endTime = t.time()
	if (endTime - startTime < 61):
		t.sleep(70 - ( endTime - startTime ))
print(count)

f.close()
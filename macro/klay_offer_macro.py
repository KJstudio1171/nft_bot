import pyautogui as p
import time as t
import defalutFunction as df

x, y = p.position()
print(x,y)
nft_position = [(210, 388), (457,388), (647,388), (920,388), (1165,388)]
make_offer_position1 = (716,472)
make_offer_position2 = (557,557)
information_position = (382, 695)
sign_position1 = (368, 483)
sign_position2 = (260, 559)
back_page_position = (20,62)
empty_position = (1252, 655)
wklay_position = (593,332)



def offer_nft(nft_position):
	p.moveTo(nft_position)
	df.click_wait(nft_position, 2)
	df.click_wait(make_offer_position1, 2)
	df.click_wait(information_position, 2)
	df.click_wait(wklay_position, 0)
	p.typewrite('50')
	df.click_wait(make_offer_position2, 2)
	df.click_wait(sign_position1, 2)
	df.click_wait(sign_position2, 2)
	df.click_wait(back_page_position, 6)

for _ in range(19) :
	for l in nft_position:
		offer_nft(l)
	df.click_wait(empty_position, 0)
	for _ in range(9):
		p.press('down')
		t.sleep(0.2)
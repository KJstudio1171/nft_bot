import bot_init
import pyautogui as p
from PIL import ImageGrab

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = bot_init.chromedriverMaker()

try:
	element = WebDriverWait(driver, 140, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'#root div input'))
	)
except Exception as e:
	print('no element')

element.send_keys('1')

screen = ImageGrab.grab()

start = (918, 243)
end = (1683, 960)
c_black = (34,34,34)

SB = 1
click = 0

for i in range(start[0], end[0], 10):
	for j in range(start[1], end[1], 10):
		rgb = screen.getpixel((i,j))
		if abs(rgb[0] - c_black[0]) + abs(rgb[1] - c_black[1]) +abs(rgb[2] - c_black[2] < 80) :
			rgb = screen.getpixel((i + 30, j))
			if abs(rgb[0] - c_black[0]) + abs(rgb[1] - c_black[1]) + abs(rgb[2] - c_black[2]) < 80:
				p.click((i + 30, j + 10))
				click = 1
				break
	if click == 1:
		break

try:
	element2 = WebDriverWait(driver, 10, 0.1).until(
		EC.element_to_be_clickable((By.LINK_TEXT,'주문'))
	)
except Exception as e:
	print('no element')

element2.click()

# try:
# 	element = WebDriverWait(driver, 10, 0.2).until(
# 		EC.presence_of_element_located((By.LINK_TEXT,'구매 가격 제안'))
# 	)
# 	print(element)
# except Exception as e:
# 	print('no element')
# element.click()

# try:
# 	element2 = WebDriverWait(driver, 10, 0.2).until(
# 		EC.presence_of_element_located((By.TAG_NAME,'input'))
# 	)
# 	print(element2)
# except Exception as e:
# 	print('no element')

# element2.send_keys('1000')

# try:
# 	element3 = WebDriverWait(driver, 10, 0.2).until(
# 		EC.presence_of_element_located((By.TAG_NAME,'label'))
# 	)
# 	print(element3)
# except Exception as e:
# 	print('no element')

# element3.click()

# try:
# 	element4 = WebDriverWait(driver, 10, 0.2).until(
# 		EC.element_to_be_clickable((By.LINK_TEXT,'구매 가격 제안 확인'))
# 	)
# 	print(element4)
# except Exception as e:
# 	print('no element')

# element4.click()
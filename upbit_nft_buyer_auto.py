import bot_init
import pyautogui as p
from PIL import ImageGrab

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = bot_init.chromedriverMaker()

try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'#root div input'))
	)
except Exception as e:
	print('no element')

element.send_keys('1')

try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'#root div.DetailPage__buttonArea a'))
	)
except Exception as e:
	print('no element')

element.click()

try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'div.DivideContent__checkbox.StyleCheckbox label'))
	)
except Exception as e:
	print('no element')

element.click()

try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'div.QuizSection__answer > input'))
	)
except Exception as e:
	print('no element')

element.click()


try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.LINK_TEXT,'주문 확인'))
	)
except Exception as e:
	print('no element')

start = (2119, 850)
end = (2241, 970)
c_black = (34,34,34)

click = 0
while not click :
	screen = ImageGrab.grab()
	for i in range(start[0], end[0], 10):
		for j in range(start[1], end[1], 10):
			rgb = screen.getpixel((i,j))
			if abs(rgb[0] - c_black[0]) + abs(rgb[1] - c_black[1]) +abs(rgb[2] - c_black[2] < 20) :
				rgb = screen.getpixel((i + 30, j))
				if abs(rgb[0] - c_black[0]) + abs(rgb[1] - c_black[1]) + abs(rgb[2] - c_black[2]) < 20:
					p.moveTo((i + 30, j + 10))
					p.click((i + 30, j + 10))
					click = 1
					break
		if click == 1:
			break

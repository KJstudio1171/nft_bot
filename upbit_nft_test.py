import bot_init
import pyautogui as p
from PIL import ImageGrab

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = bot_init.chromedriverMaker()

try:
	element = WebDriverWait(driver, 10, 0.2).until(
		EC.presence_of_element_located((By.LINK_TEXT,'구매 가격 제안'))
	)
	print(element)
except Exception as e:
	print('no element')
element.click()

try:
	element2 = WebDriverWait(driver, 10, 0.2).until(
		EC.presence_of_element_located((By.TAG_NAME,'input'))
	)
	print(element2)
except Exception as e:
	print('no element')

element2.send_keys('1000')

try:
	element3 = WebDriverWait(driver, 10, 0.2).until(
		EC.presence_of_element_located((By.TAG_NAME,'label'))
	)
	print(element3)
except Exception as e:
	print('no element')

element3.click()

try:
	element4 = WebDriverWait(driver, 10, 0.2).until(
		EC.element_to_be_clickable((By.LINK_TEXT,'구매 가격 제안 확인'))
	)
	print(element4)
except Exception as e:
	print('no element')

element4.click()
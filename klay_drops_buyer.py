import bot_init

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as p
import time as t

driver = bot_init.chromedriverMaker()

p.moveTo(687,958)



try:
	element3 = WebDriverWait(driver, 10, 0.1).until(
		EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'구매하기'))
	)
except Exception as e:
	print('no element')
element3.click()

try:
	element3 = WebDriverWait(driver, 2, 0.1).until(
		EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'양수도계약'))
	)
except Exception as e:
	print('no element')
element3.click()

p.scroll(-4000)

try:
	element3 = WebDriverWait(driver, 2, 0.1).until(
		EC.element_to_be_clickable((By.LINK_TEXT,'동의하기'))
	)
except Exception as e:
	print('no element')

element3.click()

try:
	element3 = WebDriverWait(driver, 2, 0.1).until(
		EC.element_to_be_clickable((By.LINK_TEXT,'확인'))
	)
except Exception as e:
	print('no element')

element3.click()

p.moveTo(281,747)
p.click()
p.moveTo(276,810)
p.click()
p.moveTo(276,892)
p.click()

try:
	element3 = WebDriverWait(driver, 2, 0.1).until(
		EC.element_to_be_clickable((By.LINK_TEXT,'결제하기'))
	)
except Exception as e:
	print('no element')

element3.click()
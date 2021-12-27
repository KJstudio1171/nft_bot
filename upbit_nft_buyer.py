import bot_init

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

# try:
# 	element2 = WebDriverWait(driver, 10, 0.1).until(
# 		EC.element_to_be_clickable((By.LINK_TEXT,'주문'))
# 	)
# except Exception as e:
# 	print('no element')

# element2.click()

try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'#root div label'))
	)
except Exception as e:
	print('no element')

element.click()

try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'#root div input'))
	)
except Exception as e:
	print('no element')

element.click()
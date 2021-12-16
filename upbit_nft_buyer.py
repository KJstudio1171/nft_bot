import bot_init

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = bot_init.chromedriverMaker()

# try:
# 	element = WebDriverWait(driver, 10, 0.1).until(
# 		EC.presence_of_element_located((By.CSS_SELECTOR,'#root > div > div > main > div > div.DetailPage__layout > section.DetailPage__aside > article:nth-child(1) > div:nth-child(1) > div > a.StyleButton.StyleButton--line.Tooltip.Tooltip--hiddenIcon'))
# 	)
# except Exception as e:
# 	print('no element')

# element.click()

try:
	element = WebDriverWait(driver, 20, 0.1).until(
		EC.presence_of_element_located((By.TAG_NAME,'#root div input'))
	)
except Exception as e:
	print('no element')

element.send_keys('1')

try:
	element2 = WebDriverWait(driver, 10, 0.1).until(
		EC.element_to_be_clickable((By.LINK_TEXT,'입찰'))
	)
except Exception as e:
	print('no element')

element2.click()
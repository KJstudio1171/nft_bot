import bot_init

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = bot_init.chromedriverMaker()

# try:
# 	element2 = WebDriverWait(driver, 10, 0.2).until(
# 		EC.presence_of_element_located((By.CSS_SELECTOR,'#__APP > div > div.css-tq0shg > main > div > div.css-aghwyv > div.css-1sn9i95 > div.css-bsjx8j button'))
# 	)
# 	print(element2)
# except Exception as e:
# 	print('no element')

try:
	Buy = WebDriverWait(driver, 120, 0.1).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR,'#__APP > div > div.css-tq0shg > main > div > div.css-aghwyv > div.css-1sn9i95 > div.css-bsjx8j button'))
	)
except Exception as e:
	print('no element')

Buy.click()

# for _ in range(0,10):
# 	try: 
# 		element4.click()
# 		time.sleep(0.1)
# 	except:
# 		try:
# 			element4 = WebDriverWait(driver, 10, 0.2).until(
# 				EC.element_to_be_clickable((By.CSS_SELECTOR,'#__APP > div > div.css-tq0shg > main > div > div.css-aghwyv button'))
# 			)
# 			continue
# 		except Exception as e:
# 			print('no element')

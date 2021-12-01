import platform
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
options.add_argument("app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
if platform.system() == 'Windows':
	chrome_driver = "C:\\programming\\KJstudio\\program\\project\\klay_offer_macro\\chromedriver\\windows\\chromedriver"
elif platform.system() == 'Darwin':
	chrome_driver = "C:\\programming\\KJstudio\\program\\project\\klay_offer_macro\\chromedriver\\mac\\chromedriver"
else:
	print('platform error')
driver = webdriver.Chrome(chrome_driver, options=options)

# try:
# 	element2 = WebDriverWait(driver, 10, 0.2).until(
# 		EC.presence_of_element_located((By.CSS_SELECTOR,'#root div input'))
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

try:
	element4 = WebDriverWait(driver, 120, 0.1).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR,'#__APP > div > div.css-tq0shg > main > div > div.css-aghwyv button'))
	)
except Exception as e:
	print('no element')

for _ in range(0,10):
	try: 
		element4.click()
		time.sleep(0.1)
	except:
		try:
			element4 = WebDriverWait(driver, 10, 0.2).until(
				EC.element_to_be_clickable((By.CSS_SELECTOR,'#__APP > div > div.css-tq0shg > main > div > div.css-aghwyv button'))
			)
			continue
		except Exception as e:
			print('no element')

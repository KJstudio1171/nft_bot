import platform
import os
import chromedriver_autoinstaller as CA
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
options.add_argument("app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")

chrome_ver = str(CA.get_chrome_version().split('.')[0])
platformType = platform.system()


def dirMaker(platformType:str):
	cwd = os.getcwd()
	dir = "//".join([cwd, "chromedriver", platformType])
	return dir

def chromedriverMaker():
	dir = dirMaker(platformType)
	chrome_driver = "//".join([dir, chrome_ver, "chromedriver.exe"])
	try:
		driver = webdriver.Chrome(chrome_driver, options=options)
	except:
		CA.install(False, dir)
		driver = webdriver.Chrome(chrome_driver, options=options)
	return driver

def runChromeDebuggingMode():
	if platformType == "Windows":
		os.chdir('C:\Program Files\\Google\\Chrome\\Application')
		os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"')
	elif platformType == "Darwin":
		os.chdir('/Applications/Google Chrome.app/Contents/MacOS')
		print(os.getcwd())
		os.system('./Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"')
	else:
		raise Exception("platform Error")

if __name__ == "__main__":
	runChromeDebuggingMode()
	quit()

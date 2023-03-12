import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.apple.com/"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)
browser.refresh()
time.sleep(3)
browser.get_screenshot_as_file("apple1.png")
browser.get(url="https://www.samsung.com/")
time.sleep(5)
browser.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://openai.com/")
time.sleep(5)

driver.save_screenshot("screenshot_test.png")
time.sleep(3)

driver.quit()



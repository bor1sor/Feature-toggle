
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# открываем браузер и переходим на сайт
link = "https://www.amazon.com/"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)

# обновляем страницу
browser.refresh()
time.sleep(3)

# делаем скриншот
browser.save_screenshot("screenshot123.png")
time.sleep(5)

# закрываем браузер
browser.quit()
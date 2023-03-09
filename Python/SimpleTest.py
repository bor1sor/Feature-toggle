import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.decathlon.ru/"
browser = webdriver.Chrome()
browser.get(link)

search_str = browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/header/div[1]/div/div[2]/div/div/label/div/div/input')
search_str.send_keys("Кроссовки")
time.sleep(5)
button = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/header/div[1]/div/div[2]/div/div/button[2]').click()
time.sleep(3)
check = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/main/div/div/div[2]/div/h1').text
print(check)

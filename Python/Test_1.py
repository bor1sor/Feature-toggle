import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from auth_data import cargo_numbers

link = "https://coursehunter.net/sign-in"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)

email_input = browser.find_element("id", "email")
email_input.send_keys("Your Email")

time.sleep(5)
password_input = browser.find_element("id", "password")
password_input.send_keys("Your Password")

time.sleep(5)
premium_link = browser.find_element(By.XPATH,"/html/body/header/div/div[2]/a").click()

time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/form/div[5]/button').click()

time.sleep(5)

browser.quit()

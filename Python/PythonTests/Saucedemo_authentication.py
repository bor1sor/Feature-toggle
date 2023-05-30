import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def first_test():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")

    input_username = browser.find_element(By.XPATH, '//*[@id=\"user-name\"]')
    input_password = browser.find_element(By.XPATH, '//*[@id=\"password\"]')
    login_button = browser.find_element(By.XPATH, '//*[@id=\"login-button\"]')
    time.sleep(5)

    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)
    time.sleep(5)

    title_text = browser.find_element(By.XPATH, '//*[@id=\"header_container\"]/div[2]/span')
    if title_text.text == "Products":
        print("Main page")
    else:
        print("Element not found")

    time.sleep(5)


if __name__ == '__main__':
    first_test()
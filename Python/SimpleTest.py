import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.weider.com/"
browser = webdriver.Chrome()
browser.get(link)

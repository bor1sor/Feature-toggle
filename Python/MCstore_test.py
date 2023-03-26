from selenium import webdriver
import time

options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
browser.get("https://shop.mancity.com/en/account/")
input_order = browser.find_element("id","dwfrm_trackOrder_orderNumber")
if input_order is None:
   print("Element not found")
else:
   print("Item found!")
time.sleep(5)
browser.quit()
from selenium import webdriver
from secrets import pw
import time

browser = webdriver.Firefox()
browser.get("https://www.facebook.com/")
time.sleep(3)

cookies = browser.find_element_by_id("u_0_k")
cookies.click()
time.sleep(0.1)

uname = browser.find_element_by_id("email")
pasword = browser.find_element_by_id("pass")
button = browser.find_element_by_id("u_0_b")
time.sleep(1)

uname.send_keys("email")
pasword.send_keys(pw)


time.sleep(0.1)
button.click()
time.sleep(60)

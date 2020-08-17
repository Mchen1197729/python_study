from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 需要引入 keys 包

chrome = webdriver.Chrome()

chrome.get('http://localhost:3000')
chrome.maximize_window()

print('****************')
# print(chrome.get_screenshot_as_png())

img_bytes = chrome.get_screenshot_as_png()
with open('./screen1.png', 'wb') as f1:
    f1.write(img_bytes)

username = chrome.find_element_by_css_selector("input[type=text]")
username.send_keys('chenMM')
password = chrome.find_element_by_css_selector("input[type=password]")
password.send_keys('guessmiao20ebz')
submit = chrome.find_element_by_css_selector('button[type=submit]')
submit.send_keys(Keys.ENTER)

chrome.close()

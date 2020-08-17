from selenium import webdriver
import time

chrome = webdriver.Chrome()
# print(chrome)
chrome.get('http://localhost:63342/test-of-MDN/index.html?_ijt=lss8kfnk9ljkbe6c32k6847drm')

chrome.find_element_by_css_selector('span[innerText=hello world]').click()
#
time.sleep(2)
# 关闭浏览器
chrome.quit()

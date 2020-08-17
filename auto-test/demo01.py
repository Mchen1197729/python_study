from selenium import webdriver
import time

chrome = webdriver.Chrome()
print(chrome)
chrome.get('http://www.baidu.com')
#
time.sleep(2)
# 关闭浏览器
chrome.quit()

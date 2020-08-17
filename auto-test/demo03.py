from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 需要引入 keys 包
import time

chrome = webdriver.Chrome()

chrome.get('http://www.wanjiayun.net:9528/#/picin/luru')

chrome.maximize_window()

chrome.find_element_by_css_selector('input[type=text]').send_keys('中国')
chrome.find_element_by_css_selector('input[type=password]').send_keys('123456')
chrome.find_element_by_css_selector('button').send_keys(Keys.ENTER)

time.sleep(2)
chrome.get('http://www.wanjiayun.net:9528/#/picin/luru')
time.sleep(3)
chrome.close()

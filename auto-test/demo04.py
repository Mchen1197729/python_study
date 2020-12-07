import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys  # 需要引入 keys 包
import time


def do():
    chrome = webdriver.Chrome()

    chrome.get('http://www.taobao.com')

    chrome.maximize_window()

    inputSearch = chrome.find_element_by_id('q')

    inputSearch.clear()

    js_script = '''
    document.getElementById('q').value = 'Hello World'
    '''
    chrome.execute_script(js_script)

    time.sleep(2000)
    chrome.close()


try:
    do()
except Exception as e:
    print(e)
finally:
    do()

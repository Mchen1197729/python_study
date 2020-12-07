"""
这是针对IE浏览器进行的自动打开页面的例子
"""

import os
import time

from selenium import webdriver

IEDriverServer = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = IEDriverServer

browser = webdriver.Ie(IEDriverServer)
print(browser)
browser.get('http://www.taobao.com/')

time.sleep(2)
browser.quit()

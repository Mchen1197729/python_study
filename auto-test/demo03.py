import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys  # 需要引入 keys 包
import time


def do():
    chrome = webdriver.Chrome()

    chrome.get('http://www.wanjiayun.net:9528/#/picin/luru')

    chrome.maximize_window()

    chrome.find_element_by_css_selector('input[type=text]').send_keys('123456')
    chrome.find_element_by_css_selector('input[type=password]').send_keys('123456')
    chrome.find_element_by_css_selector('button').send_keys(Keys.ENTER)

    time.sleep(2)
    # chrome.implicitly_wait(2)
    # 跳转到照图录入页面
    chrome.get('http://www.wanjiayun.net:9528/#/picin/luru')
    # chrome.close()
    time.sleep(2)

    # 获取图片的dom容器
    # img_dom = chrome.find_element_by_css_selector('img.origin-img')

    # 执行js代码
    # js = '''
    # const img_src = document.querySelector('img.origin-img').src
    # console.log(img_src)
    # '''

    # while True:
    # 点击上岗按钮
    while True:
        chrome.find_element_by_id('taskBtn').send_keys(Keys.ENTER)
        time.sleep(2)
        btn_text = chrome.find_element_by_id('taskBtn').text
        if btn_text == '离岗并提交':
            time.sleep(2)
            action = ActionChains(chrome)
            # 获取图片的src属性
            img_src = chrome.find_element_by_css_selector('img.origin-img').get_attribute('src')
            print(img_src)
            time.sleep(1)
            blank_input = chrome.find_element_by_css_selector('.wordluru input')
            # 先清空输入框的值
            blank_input.clear()
            action.move_to_element(blank_input).click(blank_input)
            # 直接操作js去改变输入框的值
            js_script = '''
                let blank_input = document.querySelector(".wordluru input")
                blank_input.value = "测试中文123abc"
                blank_input.dispatchEvent(new Event("input"))
            '''
            chrome.execute_script(js_script)
            time.sleep(2)
            # 点击提交按钮
            chrome.find_element_by_id('taskBtn').send_keys(Keys.ENTER)
            time.sleep(3)
            # break

    # print(img_dom)


try:
    do()
except Exception as e:
    print(e)
finally:
    do()

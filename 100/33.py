# -*- coding: utf-8 -*-
#!/usr/bin/env python

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

driver.execute_script("window.alert('这是一个alert弹框。');")

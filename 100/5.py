# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 问题:定义一个至少有两个方法的类:        getString:从控制台输入获取字符串        printString::打印大写母的字符串。
# 还请包含简单的测试函数来测试类方法。
# 提示:使用_init__方法构造一些参数
import re
class GetAndPrint:
    def __init__(self):
        self.ss = ''
    def getString(self):
        self.ss = input('请输入一些内容：')
    def printString(self):
        ss2 = ''.join(re.findall('[A-Z]+',self.ss))
        ss3 = self.ss.upper()
        print(ss2,ss3)

A = GetAndPrint()
A.getString()
A.printString()
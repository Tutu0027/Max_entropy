# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 题：编写一个接受句子的程序，并计算大写字母和小写字母的数量。
# 假设为程序提供了以下输入：
# Hello world!
# 然后，输出应该是：
# 大写实例 1
# 小写实例 9
def count_num(ss):
    upper_num = 0
    low_num = 0
    for i in ss:
        if i.isupper():
            upper_num +=1
        elif i.islower():
            low_num  +=1
    print(upper_num,low_num)
count_num('Hello world!')

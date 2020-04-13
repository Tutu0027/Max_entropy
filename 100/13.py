# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 题：编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
# # Hello world! 123
# # 然后，输出应该是：
# # 字母10
# # 数字3
def count_num(ss):
    char_num = 0
    digt_num = 0
    ss.strip()
    for i in ss:
        if i.isdigit():#判断是否数字
            digt_num +=1
        elif i.isalpha():#判断是否字母
            char_num +=1
    print(char_num,digt_num)
count_num('Hello world! 123')
# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
# # 则输出为:40320
# # 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。

# def countsome(input_num):
#     sum = 1
#     for i in range(1,input_num+1):
#         sum = sum * i
#     return sum
# n = int(input("请输入一个正整数:"))#控制台输入都是str,请注意转换类型
# print(countsome(n))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
while True:
    try:
        text = input('请输入一个正整数：')
        num = int(text)
    except ValueError:
        print('您输入的不是数字')
        continue
    print(fact(num))
    break





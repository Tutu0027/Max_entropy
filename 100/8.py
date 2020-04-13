# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 问题:编写一个程序，接受逗号分隔的单词序列作为输入，按字母顺序排序后按逗号分隔的序列打印单词。假设向程序提供以下输入:
# # without,hello,bag,world
# # 则输出为:
# # bag,hello,without,world
# # 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
# ss = input('请输入：')
# ll = ss.split(',')
# ll.sort()
# for i in ll:
#     print(i,end=',')

items = [x for x in input('请输入:').split(',')]
items.sort()
print(','.join(items))
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 题：编写一个程序来计算输入中单词的频率。 按字母顺序对键进行排序后输出。
freq = {}  # frequency of words in text
print("请输入：")
line = input()
for word in line.split():
    #字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。
    freq[word] = freq.get(word, 0) + 1
words = sorted(freq.keys())  # 按key值对字典排序

for w in words:
    print("%s:%d" % (w, freq[w]))

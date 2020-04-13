# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 问题:编写一个程序，接受一行序列作为输入，并在将句子中的所有字符大写后打印行。
# 假设向程序提供以下输入:
# Hello world
# Practice makes perfect
# 则输出为:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。

lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)

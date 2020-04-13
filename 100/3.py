# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 问题:使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
# 假设向程序提供以下输入:8
# 则输出为:
# {1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。考虑使用dict类型()

def switch_to_dict(n):
    dict ={}
    for i in range(1, n+1):
        dict[i] = i*i
    print(dict)

switch_to_dict(8)
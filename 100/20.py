# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 题：使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
# #
# # 提示：考虑使用yield。

def give_7(n):
    while n > 0:
        if n % 7 ==0:
            yield n
        n = n-1
for i in give_7(98):
    print(i)
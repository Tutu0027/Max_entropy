# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
L=[]
a =[1,2,3,4]

for i in a:
    for j in a:
        for k in a:
            if (k==j or j==i or i==k):
                continue
            else:
                L.append(str(i)+str(j)+str(k))
print(L)
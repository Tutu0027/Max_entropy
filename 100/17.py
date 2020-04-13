# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 题：编写一个程序，根据控制台输入的事务日志计算银行帐户的净金额。 事务日志格式如下所示：
# D 100
# W 200
# D表示存款，而W表示提款。
# 假设为程序提供了以下输入：
# D 300
# D 300
# W 200
# D 100
# 然后，输出应该是：
# 500
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
lines = []
while True:
    ss = input('请输入：')
    if ss:
        lines.append(ss)
        continue
    else:
        break
num = 0
for i in lines:
    ll = i.split(' ')
    if ll[0] == 'D':
        num = num + int(ll[1])
    if ll[0] == 'W':
        num = num -int(ll[1])
print(num)

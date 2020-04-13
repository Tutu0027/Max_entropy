# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 题：您需要编写一个程序，按升序对（名称，年龄，高度）元组进行排序，其中name是字符串，age和height是数字。 元组由控制台输入。 排序标准是：
# 1：根据名称排序;
# 2：然后根据年龄排序;
# 3：然后按分数排序。
# 优先级是name> age>得分。
# 如果给出以下元组作为程序的输入：
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# 然后，程序的输出应该是：
# [（'John'，'20'，'90'），（'Jony'，'17'，'91'），（'Jony'，'17'，'93'），（'Json'，'21 '，'85'），（'Tom'，'19'，'80'）]
#
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。我们使用itemgetter来启用多个排序键。

from operator import itemgetter, attrgetter
ll=[('Tom',19,80),('John',20,90),('Jony',17,91),('Jony',17,93),('Json',21,85)]
print(sorted(ll,key=itemgetter(0,1,2)))
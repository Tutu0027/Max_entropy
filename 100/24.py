# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 题：Python有许多内置函数，如果您不知道如何使用它，您可以在线阅读文档或查找一些书籍。 但是Python为每个内置函数都有一个内置的文档函数。
#      请编写一个程序来打印一些Python内置函数文档，例如abs（），int（），raw_input（）
#      并为您自己的功能添加文档
#     
# 提示：内置文档方法是__doc__
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    '''Return the square value of the input number.
    The input number must be integer.
    '''
    return num ** 2


print(square(2))
print(square.__doc__)
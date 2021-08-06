#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-28 11:49
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : build_queue_using_array.py
# @Software : PyCharm
# @Desc     : 用数组实现队列
"""

queue = []

queue.append(1)
queue.append(2)
queue.append(3)

# x = queue.pop(-1)
# x = queue.pop()
a = queue.pop(0)
print(a)
b = queue.pop(0)
print(b)
queue.append(4)
c = queue.pop(0)
print(c)
queue.append(5)

print(queue)

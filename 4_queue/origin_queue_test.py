#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-04 17:05
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : origin_queue_test.py
# @Software : PyCharm
# @Desc     :
"""
from multiprocessing import Queue
# from queue import Queue

"""
像栈一样，队列（4_queue）也是表，然后，使用队列时插入在一端进行而删除则在另一端进行。
队列的基本操作是Enqueue（入队），它是在表的末端（叫做队尾（rear））插入一个元素，还有Dequeue（出队），它是删除在表的开头（叫做队头（front））的元素。
                      ________
                     |        |
                     |        |
<----Dequeue(Q)------|Queue(Q)|<------Enqueue(Q,X)------
                     |        |
                     |________|
"""

q = Queue(3)  # 当队列已满,继续放值,,会阻塞程序
q.put(1)
q.put(2)
q.put(3)
pass
# q.put(4)  # 当队列已满,继续放值,,会阻塞程序
try:
    q.put_nowait(4)  # 等同于 q.put(4, False)
except:
    print("队列已经满了.")

print(q.get())
print(q.get())
print(q.get())
# print(q.get())  # 当队列空了,继续取值,也会阻塞程序
try:
    q.get_nowait()  # 等同于q.get(block=False)
except:
    print("队列已经空了.")
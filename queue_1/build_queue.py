#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-04 17:05
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : build_queue.py
# @Software : PyCharm
# @Desc     :
"""

"""
像栈一样，队列（queue_1）也是表，然后，使用队列时插入在一端进行而删除则在另一端进行。
队列的基本操作是Enqueue（入队），它是在表的末端（叫做队尾（rear））插入一个元素，还有Dequeue（出队），它是删除在表的开头（叫做队头（front））的元素。
                      ________
                     |        |
                     |        |
<----Dequeue(Q)------|Queue(Q)|<------Enqueue(Q,X)------
                     |        |
                     |________|
"""
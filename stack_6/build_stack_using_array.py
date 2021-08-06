#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-28 14:46
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : build_stack_using_array.py
# @Software : PyCharm
# @Desc     : 栈是有序的LIFO(后进先出)
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        """
        入栈
        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """
        栈顶元素出栈
        :return:
        """
        return self.items.pop()

    def peek(self):
        """
        打印栈顶元素
        :return:
        """
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

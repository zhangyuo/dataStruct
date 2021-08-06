#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-04-07 09:31
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : JZ_3.py
# @Software : PyCharm
# @Desc     :
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        if listNode.next is None:
            return [listNode.val]
        prev = None
        curr = listNode
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tmp = []
        tmp.append(prev.val)
        while prev.next:
            prev = prev.next
            tmp.append(prev.val)
        return tmp


class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]


if __name__ == "__main__":
    val0 = ListNode(0)
    val1 = ListNode(1)
    val2 = ListNode(2)
    val3 = ListNode(3)
    val4 = ListNode(4)
    val5 = ListNode(5)

    s = Solution()
    result = s.printListFromTailToHead(val5)
    print(result)

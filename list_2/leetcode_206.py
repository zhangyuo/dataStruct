#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-04-01 15:01
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : leetcode_206.py
# @Software : PyCharm
# @Desc     :
"""
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList_1(head):
    num = []
    if not head:
        return head
    if not head.next:
        return head
    num.append(head.val)
    while head.next:
        head = head.next
        num.append(head.val)

    new_head = None
    for i in num:
        new_head = ListNode(i, new_head)

    return new_head


def reverseList(head):
    if not head:
        return head
    if not head.next:
        return head
    prev = None
    curr = head
    prev = ListNode(curr.val, prev)
    while curr.next:
        curr = curr.next
        prev = ListNode(curr.val, prev)

    return prev


if __name__ == "__main__":
    val0 = ListNode(0, None)
    val1 = ListNode(1, val0)
    val2 = ListNode(2, val1)
    val3 = ListNode(3, val2)
    val4 = ListNode(4, val3)
    val5 = ListNode(5, val4)
    result = reverseList(val5)
    print(result)

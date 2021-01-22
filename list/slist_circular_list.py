#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-04 16:57
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : slist_circular_list.py
# @Software : PyCharm
# @Desc     : 单向循环链表
"""

"""
单向循环链表：在单链表的基础上，再多一个由尾节点指向首节点的链接，首节点是指链表的第一个存数据的结点，
而头结点是指指向第一个存数据的结点的那个东西，仅有个链接域，而不是真正存储内容的链表结点。需要注意的是，循环链表中，
一些功能的创建是和单链表不一样的，比如判空、判满，它是循环的该怎么判断呢？这些内容可以在上面给出的单链表的实现中进行修改获得，可以试一下。
"""

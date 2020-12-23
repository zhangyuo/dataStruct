#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2020-04-08 14:16
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : 0_tree_node.py
# @Software : PyCharm
# @Desc     :
"""

"""
创建一个 TreeNode 的类，作为基础数据结构：链点，并初始化对应的内参
"""


class TreeNode(object):

    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.item)

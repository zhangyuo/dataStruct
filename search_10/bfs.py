#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-02-23 11:08
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : bfs.py
# @Software : PyCharm
# @Desc     : 广度优先搜索：先搜索邻居，搜索完邻居再搜邻居的邻居。
"""
from tree_3.tree_build.tree_node import TreeNode

"""
两个思想：
1、队列不为空，则循环
2、将未访问的邻接点压入队列后面，然后从前面依次访问
图：
0
1 2
3 4 5 6
遍历顺序：0123456

用途：
用于搜索最短路径的解

数据结构：
队列
"""


def bfs_1(root):
    """
    广度优先遍历:树
    :param node:
    :return:
    """
    queue = []
    queue.append(root)

    while queue:
        # 第一个出栈
        node = queue.pop(0)
        print(node.item)
        # 先进先出
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    """
        定义一个二叉搜索树
                      18
                13          21
            7      15   19      100
        3      10
        """
    tree = TreeNode(18, TreeNode(13, TreeNode(7, TreeNode(3), TreeNode(10)), TreeNode(15)),
                    TreeNode(21, TreeNode(19), TreeNode(100)))
    bfs_1(tree)

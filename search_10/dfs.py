#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-02-23 11:08
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : dfs.py
# @Software : PyCharm
# @Desc     : 深度优先搜索：是一种利用递归实现的搜索算法。从起点出发，先把一个方向的带你都遍历完才会改变方向。
"""
from tree_3.tree_build.tree_node import TreeNode

"""
图：
0
1 2
3 4 5 6
搜索顺序：0134256

用途：
DFS空间效率高，适合搜索全部的解

数据结构：
栈
"""


def dfs(g, i, j):
    """
    深度优先遍历:二维数组(图)
    :param g:
    :param i:
    :param j:
    :return:
    """
    g_len = len(g)
    if i >= 0 and j >= 0 and i < g_len and j < g_len and g[i][j] == 0:
        g[i][j] = 1
        dfs(g, i - 1, j)
        dfs(g, i + 1, j)
        dfs(g, i, j - 1)
        dfs(g, i, j + 1)


def dfs_1(root):
    """
    深度优先遍历:树
    :param node:
    :return:
    """
    stack = []
    stack.append(root)

    while stack:
        # 最后一个出栈
        node = stack.pop()
        print(node.item)
        # 后进先出
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

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
    dfs_1(tree)

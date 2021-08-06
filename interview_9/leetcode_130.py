#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2020-02-05 17:24
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : test2.py
# @Software : PyCharm
# @Desc     : 字节面试-leetcode-130. 被围绕的区域：把所有被0包围的1转化为0（连通图）
"""
"""
首先对边界上每一个'1'做深度优先搜索，将与其相连的所有'1'改为'-'。然后遍历矩阵，将矩阵中所有'1'改为'0',将矩阵中所有'-'变为'1' 
"""


class Solution:
    def regionsBySlashes(self, grid):
        """
        深度优先搜索
        :type grid: List[str]
        :rtype: int
        """
        g_len = len(grid)
        if g_len == 0:
            return None
        g_2_len = len(grid[0])

        def dfs(g, i, j):
            """
            深度优先遍历
            :param g:
            :param i:
            :param j:
            :return:
            """
            if i >= 0 and j >= 0 and i < g_len and j < g_2_len and g[i][j] == 1:
                g[i][j] = "-"
                dfs(g, i - 1, j)
                dfs(g, i + 1, j)
                dfs(g, i, j - 1)
                dfs(g, i, j + 1)

        for i in range(g_2_len):
            if grid[0][i] == 1:
                dfs(grid, 0, i)
            if grid[g_len - 1][i] == 1:
                dfs(grid, g_len - 1, i)

        for i in range(g_len):
            if grid[i][0] == 1:
                dfs(grid, i, 0)
            if grid[i][g_2_len - 1] == 1:
                dfs(grid, i, g_2_len - 1)

        for i in range(g_len):
            for j in range(g_2_len):
                if grid[i][j] == 1:
                    grid[i][j] = "x"
                if grid[i][j] == "-":
                    grid[i][j] = 1

        return None


if __name__ == "__main__":
    L = [
        [0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0]
    ]
    # L = [
    #     [0, 0, 0, 0],
    #     [0, 1, 1, 0],
    #     [0, 0, 1, 0],
    #     [0, 1, 0, 0]
    # ]
    m = Solution()
    num = m.regionsBySlashes(L)
    print(L)

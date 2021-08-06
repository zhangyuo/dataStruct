#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-26 13:59
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : Leetcode_959.py
# @Software : PyCharm
# @Desc     : Leetcode 959：由斜杠划分区域
"""


class Solution:
    def regionsBySlashes(self, grid):
        """
        深度优先搜索
        :type grid: List[str]
        :rtype: int
        """
        grid_len = len(grid)
        if grid_len == 0:
            return 0
        g_len = grid_len * 3
        g = [[0] * g_len for _ in range(g_len)]

        def dfs(g, i, j):
            """
            深度优先遍历
            :param g:
            :param i:
            :param j:
            :return:
            """
            if i >= 0 and j >= 0 and i < g_len and j < g_len and g[i][j] == 0:
                g[i][j] = 1
                dfs(g, i - 1, j)
                dfs(g, i + 1, j)
                dfs(g, i, j - 1)
                dfs(g, i, j + 1)

        for i in range(grid_len):
            for j in range(grid_len):
                if grid[i][j] == '/':
                    g[i * 3 + 2][j * 3], g[i * 3 + 1][j * 3 + 1], g[i * 3][j * 3 + 2] = 1, 1, 1
                if grid[i][j] == '\\':
                    g[i * 3][j * 3], g[i * 3 + 1][j * 3 + 1], g[i * 3 + 2][j * 3 + 2] = 1, 1, 1

        res = 0
        for i in range(g_len):
            for j in range(g_len):
                if g[i][j] == 0:
                    dfs(g, i, j)
                    res += 1

        return res


class Solution1:
    def regionsBySlashes(self, grid):
        """
        并查集
        :type grid: List[str]
        :rtype: int
        """
        s = dict()

        def find(x):
            s.setdefault(x, x)
            if s[x] != x:
                s[x] = find(s[x])

            return s[x]

        def union(x, y):
            s[find(x)] = find(y)

        grid_len = len(grid)
        for i in range(grid_len):
            for j in range(grid_len):
                if i:
                    union((i, j, 0), (i - 1, j, 2))
                if j:
                    union((i, j, 3), (i, j - 1, 1))
                if grid[i][j] != '/':
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 3), (i, j, 2))
                if grid[i][j] != '\\':
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 2), (i, j, 1))

        return len(set(map(find, s)))


if __name__ == "__main__":
    grid = [
        "/\\",
        "\\/"
    ]
    m = Solution1()
    num = m.regionsBySlashes(grid)
    print("分割的独立区域数:", num)

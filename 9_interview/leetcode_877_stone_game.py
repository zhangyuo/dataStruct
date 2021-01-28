#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-28 09:16
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : leetcode_877_stone_game.py
# @Software : PyCharm
# @Desc     :
"""


class Solution:
    def stoneGame(self, arr):
        n = len(arr)
        dp = [0] * n
        for i in range(0, n):
            dp[i] = [(0, 0)] * n
        # 边界条件
        for i in range(0, n):
            dp[i][i] = (arr[i], 0)
        # dp数组的迭代解法
        for k in range(0, n):
            for j in range(k + 1, n):
                # 斜线遍历
                i = j - (k + 1)
                # 先手拿左边
                left = arr[i] + dp[i + 1][j][1]
                # 先手拿右边
                right = arr[j] + dp[i][j - 1][1]
                if left > right:
                    dp[i][j] = (left, dp[i + 1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j - 1][0])

        (a, b) = dp[0][len(arr) - 1]
        if a > b:
            return True
        else:
            return False


if __name__ == "__main__":
    m = Solution()
    arr = [2, 4, 58, 23, 56, 1, 46]
    print(m.stoneGame(arr))

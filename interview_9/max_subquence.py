#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-27 14:23
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : max_subquence.py
# @Software : PyCharm
# @Desc     :
"""


def solution(arr):
    """
    动态规划：给定一个无需整数数列，找到最长上升子序列的长度
    :param arr:
    :return:
    """
    n = len(arr)
    dp = [1] * n

    for i in range(0, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    res = 0
    for i in range(0, n):
        res = max(res, dp[i])
    return res


if __name__ == "__main__":
    arr = [1, 4, 3, 4, 2]
    num = solution(arr)
    print(num)

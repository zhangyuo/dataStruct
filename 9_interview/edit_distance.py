#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-27 15:45
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : edit_distance.py
# @Software : PyCharm
# @Desc     :
"""


def minDistance(word1, word2):
    result = {}

    def dp(i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if result and (i, j) in result:
            return result[(i, j)]
        if word1[i] == word2[j]:
            result[(i, j)] = dp(i - 1, j - 1)
            return result[(i, j)]
        else:
            result[(i, j)] = min(
                dp(i, j - 1) + 1,
                dp(i - 1, j) + 1,
                dp(i - 1, j - 1) + 1
            )
            return result[(i, j)]

    return dp(len(word1) - 1, len(word2) - 1)


if __name__ == "__main__":
    num = minDistance('horse', 'ros')
    print(num)

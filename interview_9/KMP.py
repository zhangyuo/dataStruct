#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-02-03 10:55
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : KMP.py
# @Software : PyCharm
# @Desc     : 字符串匹配
"""


def KMP(pat):
    m = len(pat)
    dp = [0] * m
    for i in range(0, m):
        # ascii 字符数 = 256
        dp[i] = [0] * 256
    # init state
    dp[0][ord(pat[0])] = 1
    # 影子状态
    x = 0
    for i in range(1, m):
        for c in range(0, 256):
            if ord(pat[i]) == c:
                dp[i][c] = i + 1
            else:
                dp[i][c] = dp[x][c]
        x = dp[x][ord(pat[i])]
    return dp


def match_text(text, pat):
    dp = KMP(pat)
    n = len(text)
    m = len(pat)
    j = 0
    for i in range(0, n):
        j = dp[j][ord(text[i])]
        if j == m:
            return i - m + 1
    return -1


if __name__ == "__main__":
    text = "ABABDABABC"
    pat = "ABABC"
    print(match_text(text, pat))

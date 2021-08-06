#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-02-05 17:28
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : house_robber_1.py
# @Software : PyCharm
# @Desc     : 打家劫舍-leetcode-198 & 213
"""


def max_profit(a):
    n = len(a)
    if n == 0:
        return 0
    dp = [0] * n
    for k in range(0, n):
        dp[k] = [0] * 2

    for i in range(0, n):
        if i == 0:
            dp[0][0] = 0
            dp[0][1] = a[i]
            continue
        elif i == 1:
            dp[1][0] = max(dp[0][0], dp[0][1])
            dp[1][1] = a[i]
            continue
        # 状态：位置i、行为：抢、不抢
        # 状态方程
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = max(dp[i - 1][0] + a[i], dp[i - 2][0] + a[i], dp[i - 2][1] + a[i])
    return max(dp[n - 1][0], dp[n - 1][1])


def max_profit_1(nums):
    """
    首位房子围成一个圈
    三种情况比较：a[0:n-2]/a[1:n-2]/a[1:n-1],其实比较1和3情况就行
    :param nums:
    :return:
    """
    y = len(nums)
    if y == 0:
        return 0
    elif y == 1:
        return nums[0]

    def rob(a):
        n = len(a)
        dp = [0] * n
        for k in range(0, n):
            dp[k] = [0] * 2

        for i in range(0, n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = a[i]
                continue
            elif i == 1:
                dp[1][0] = max(dp[0][0], dp[0][1])
                dp[1][1] = a[i]
                continue
            # 状态：位置i、行为：抢、不抢
            # 状态方程
            dp[i][1] = max(dp[i - 1][0] + a[i], dp[i - 2][0] + a[i], dp[i - 2][1] + a[i])
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        return max(dp[n - 1][0], dp[n - 1][1])

    return max(rob(nums[0:y-1]), rob(nums[1:y]))


if __name__ == "__main__":
    a = [2, 7, 9, 3, 1]
    a = [1, 2, 3, 1]
    a = [2, 7, 3, 1, 9]
    p = max_profit(a)
    print(p)

    a = [2, 3, 2]
    a = [1, 2, 3, 1]
    p = max_profit_1(a)
    print(p)

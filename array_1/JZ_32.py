#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-04-07 14:34
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : JZ_32.py
# @Software : PyCharm
# @Desc     :
"""
import functools


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def cmp(a, b):
            A = ""
            B = ""
            A += str(a)
            A += str(b)
            B += str(b)
            B += str(a)

            if A < B:
                return -1
            elif A > B:
                return 1
            else:
                return 0

        if not numbers:
            return ""
        numbers = list(map(str, numbers))
        numbers = sorted(numbers, key=functools.cmp_to_key(cmp))
        return ''.join(numbers)


if __name__ == "__main__":
    s = Solution()
    a = [3,5,1,4,2]
    result = s.PrintMinNumber(a)
    print(result)

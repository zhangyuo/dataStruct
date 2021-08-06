#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-02-23 14:25
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : binerary_search.py
# @Software : PyCharm
# @Desc     : 二分查找
"""


def binary_search(nums, key):
    """
    递归方式：二分查找
    :param nums:
    :param key:
    :return:
    """
    n = len(nums)
    if 0 == n:
        return False
    mid = n // 2
    if nums[mid] == key:
        return True
    elif key < nums[mid]:
        return binary_search(nums[:mid], key)
    else:
        return binary_search(nums[mid + 1:], key)


if __name__ == "__main__":
    nums = [1, 3, 8, 9, 34, 45, 56, 78, 978]
    key = 56
    print(binary_search(nums, key))

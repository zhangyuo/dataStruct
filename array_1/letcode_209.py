#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-04-01 11:36
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : letcode_209.py
# @Software : PyCharm
# @Desc     :
"""
"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minSubArrayLen(self, s, array):
        if len(array) == 0:
            return 0
        min = float('inf')
        tmp_min = 0
        index = 0
        sum = 0

        for i in range(0, len(array)):
            sum += array[i]
            tmp_min += 1
            if sum < s:
                continue
            else:
                while sum > s:
                    sum -= array[index]
                    index += 1
                    tmp_min -= 1
                    if sum < s:
                        index -= 1
                        sum += array[index]
                        tmp_min += 1
                        break
                if tmp_min < min:
                    min = tmp_min
            if min == 1:
                return 1
        if sum < s:
            return 0
        return min

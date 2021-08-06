#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-04-02 10:18
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : jz_1.py
# @Software : PyCharm
# @Desc     :
"""

"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
  [1,2,8,9],
  [2,4,9,12],
  [4,7,10,13],
  [6,8,11,15]
]
给定 target = 7，返回 true。
给定 target = 3，返回 false。
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array is None or len(array[0]) == 0:
            return False
        flag = False
        row = 0
        cloum = 0
        value = array[row][cloum]
        if value == target:
            return True

        while row < len(array) and cloum < len(array):
            if cloum + 1 < len(array):
                right = array[row][cloum + 1]
            else:
                right = value
            if right == target:
                return True

            if row + 1 < len(array):
                down = array[row + 1][cloum]
            else:
                down = value
            if down == target:
                return True

            if down > target and right > target:
                return False

            if cloum + 1 < len(array) and row + 1 < len(array):
                diagonal = array[row + 1][cloum + 1]
            else:
                diagonal = None

            if diagonal:
                if diagonal == target:
                    flag = True
                    break
                elif diagonal < target:
                    cloum += 1
                    row += 1
                    continue

            if right >= down:
                value = right
            else:
                value = down

            if value == target:
                flag = True
                break
            elif value < target:
                if value == right:
                    cloum += 1
                else:
                    row += 1
            else:
                if down == target:
                    flag = True
                    break
                if value == right:
                    row += 1
                else:
                    cloum += 1
        return flag


class Solution_1:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array is None or len(array[0]) == 0:
            return False
        flag = False
        row = 0
        cloum = 0
        value = array[row][cloum]
        if value == target:
            return True

        def find_line(nums, end_index):
            flag = False
            for i in range(0, end_index+1):
                if nums[i] == target:
                    flag = True
                elif nums[i] > target:
                    end_index = i
                    break
            return flag, end_index

        end_index = len(array[0]) - 1
        for i in range(0, len(array)):
            if array[i][0] > target:
                break
            flag, end_index = find_line(array[i], end_index)
            if flag:
                break

        return flag


if __name__ == "__main__":
    target = 15
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    method = Solution_1()
    result = method.Find(target, array)
    print(result)

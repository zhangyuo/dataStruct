#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-28 14:21
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : origin_heap_test.py
# @Software : PyCharm
# @Desc     : 堆是一个二叉树，其中每个父节点的值都小于或等于其所有子节点的值。整个堆的最小元素总是位于二叉树的根节点。
#             python的heapq模块提供了对堆的支持。堆数据结构最重要的特征是heap[0]永远是最小的元素
"""

import heapq

# heapq.heappush(heap,item)
# heap为定义堆，item增加的元素
h = []
heapq.heappush(h, 2)
print(h)

# heapq.heapify(list)
# 将列表转换为堆
list = [1, 2, 3, 5, 1, 5, 8, 9, 6]
heapq.heapify(list)
print(list)

# heapq.heapify(list)
# 删除最小值，因为堆的特征是heap[0]永远是最小的元素，所以一般都是删除第一个元素。
a = heapq.heappop(list)
print(a, list)

# heapq.heapreplace(heap.item)
# 删除最小元素值，添加新的元素值
b = heapq.heapreplace(list, 99)
print(b, list)
# 首先判断添加元素值与堆的第一个元素值对比，如果大，则删除第一个元素，然后添加新的元素值。否则不更改堆

# heapq.merge（…）
# 将多个堆合并
k = heapq.merge(h, list)
for i in k:
    print(i, end=" ")
print()

# heapq.nlargest(n,heap)
# 查询堆中的最大元素，n表示查询元素个数
c = heapq.nlargest(3, list)
print(c, list)

# heapq.nsmallest(n,heap)
# 查询堆中的最小元素，n表示查询元素的个数
d = heapq.nsmallest(3, list)
print(d)

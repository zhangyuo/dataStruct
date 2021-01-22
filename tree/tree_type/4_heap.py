#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2020-02-12 11:58
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : heap.py
# @Software : PyCharm
# @Desc     :
"""

"""
堆：又被为优先队列(priority queue_1)。尽管名为优先队列，但堆并不是队列。
结构见README.md "堆示例"

堆定义:
1 堆heap 是一个完全二叉树，完全二叉树就是只有最后一层有页子节点，而且页子节点是靠左排列的
2 每个非叶子结点都要大于或等于其左右孩子结点的值称为大顶堆
3 每个非叶子结点都要小于或者等于其左右孩子结点的值称为小顶堆
4 根节点一定是大顶堆的最大值，小顶堆中的最小值


时间复杂度分析
build_heap过程：
一共调用n次build_heap函数，而build_heap(i)的时间复杂度是O(log i)，所以整个建立大顶堆的时间复杂度是O(log1) + O(log2) + O(log3) + … O(logn) = O(n)。(注：该公式是一个定理)
heapify过程：
一共调用n次heapify，heapify()的时间复杂度是O(log n)，所以，整个不断交换堆顶与堆尾元素，并进行大顶堆化的时间复杂度是O(n*log(n))。
heap_sort过程：
整个堆排序的时间复杂度：O(n) + O(n* logn) = O(n*logn)
"""


def build_heap(arr, i):
    """
    大顶堆构建
    [3,8,5,2]:
    i=1--a[1]?a[0]; i=0
    i=2--a[2]?a[0]; i=0
    i=3--a[3]?a[1]; i=1--a[1]?a[0]; i=0
    :param arr: 输入数组
    :param i: range(1,len(arr))
    :return:
    """
    # 当子节点大于父节点时 交换
    while arr[i] > arr[(i - 1) // 2] and i > 0:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        # 继续向上交换
        i = (i - 1) // 2


def heapify(arr, i, heap_size):
    """
    修改大顶堆"根节点"的值，再次将其形成大顶堆
    :param arr
    :param i: 当前修改元素的位置
    :param heap_size: 堆大小
    :return:
    """
    # 左节点的位置
    p = 2 * i + 1
    while p < heap_size:
        # 如果右节点存在
        if p + 1 < heap_size:
            # 选出左右节点中 较大的与父节点比较
            p = p if arr[p] > arr[p + 1] else p + 1
        # 当父节点较小时 交换
        if arr[i] < arr[p]:
            arr[i], arr[p] = arr[p], arr[i]
        else:  # 否则 退出循环
            break
        i = p
        p = 2 * i + 1
    return arr


if __name__ == '__main__':

    # 1、大顶堆构建
    ##
    # 遍历数组arr，比较子节点与其父节点，若子节点大于父节点，交换二者的值。
    ##
    arr = [3, 8, 5, 2, 9, 5]
    print("输入数组：")
    print(arr)
    for i in range(1, len(arr)):
        build_heap(arr, i)
    print("大顶堆构建:")
    print(arr, "\n")

    # 2、修改大顶堆根节点的值，再次将其形成大顶堆
    ##
    # 比较1与其左孩子8和右孩子5，将其与最大的一个交换
    ##
    # 大顶堆
    arr = [9, 8, 5, 2, 3, 5]
    # 将大顶堆的第一个数修改为1
    arr[0] = 1
    arr = heapify(arr, 0, len(arr) - 1)
    print("修改大顶堆根节点的值a[0]=1，再次将其形成大顶堆:")
    print(arr, "\n")

    # 3、堆排序:大顶堆之从小到大排序
    ##
    # 堆排序思路： 首先，建立大顶堆，找到数组中的最大值；然后，交换大顶堆的根节点与最后一个叶子节点，再将前n-1个元素 构建成 大顶堆，直到仅剩一个元素为止。
    ##
    arr = [3, 8, 5, 2, 9, 5]
    # 建立大顶堆
    for i in range(1, len(arr)):
        build_heap(arr, i)
    # 不断调整堆顶元素 进行大顶堆重建
    for j in range(len(arr) - 1, 0, -1):  # j=5, 4, 3, 2, 1
        # 交换最大值至堆最后一个叶子节点
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, j)
    print("堆排序-大顶堆之从小到大:")
    print(arr)

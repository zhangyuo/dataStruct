#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-20 15:49
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : sort_methods.py
# @Software : PyCharm
# @Desc     :
"""
from utils.func_timer import func_timer


@func_timer
def insertion_sort(array):
    """
    插入排序
    基本思想：每步将一个待排序的纪录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
    算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。
    :param array:
    :return:
    """
    if len(array) < 1:
        return array
    for i in range(1, len(array)):
        tmp = array[i]
        index = i
        for j in range(i - 1, -1, -1):
            if tmp < array[j]:
                array[j + 1] = array[j]
            else:
                index = j + 1
                break
        array[index] = tmp
    return array


@func_timer
def bubble_sort(array):
    """
    冒泡排序
    基本思想：持续比较相邻的元素。如果第一个比第二个大，就交换他们两个。直到没有任何一对数字需要比较。
    冒泡排序最好的时间复杂度为O(n)。冒泡排序的最坏时间复杂度为O(n^2)。因此冒泡排序总的平均时间复杂度为O(n^2)。
    算法适用于少量数据的排序，是稳定的排序方法。
    :param array:
    :return:
    """
    if len(array) < 1:
        return array
    for i in range(len(array) - 1, 0, -1):
        flag = False  # 设置是否发生交换的标志
        for j in range(0, i):
            if array[j] > array[j + 1]:
                tmp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = tmp
                flag = True
        if not flag:
            break
    return array


@func_timer
def select_sort(array):
    """
    选择排序
    基本思想：每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。
    选择排序是不稳定的排序方法。时间复杂度 O(n^2)。
    :param array:
    :return:
    """
    if len(array) < 1:
        return array
    for i in range(0, len(array)):
        min = array[i]
        index = i
        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                index = j
        if i != index:
            array[index] = array[i]
            array[i] = min
    return array


@func_timer
def shell_sort(array):
    """
    希尔排序
    基本思想：先取一个小于n的整数d1作为第一个增量，把文件的全部记录分组。所有距离为d1的倍数的记录放在同一个组中。先在各组内进行直接插入排序；
    然后，取第二个增量d2<d1重复上述的分组和排序，直至所取的增量dt=1(dt<dt-1…<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。
    在使用增量dk的一趟排序之后，对于每一个i，我们都有a[i]<=a[i+dk],即所有相隔dk的元素都被排序。
    :param array:
    :return:
    """
    if len(array) < 1:
        return array
    gap = len(array) // 2
    while (gap):
        for i in range(gap, len(array)):
            tmp = array[i]
            index = i
            for j in range(i - gap, -1, -gap):
                if tmp < array[j]:
                    array[j + gap] = array[j]
                    index = j
                else:
                    index = j + gap
                    break
            array[index] = tmp
        gap = gap // 2
    return array


@func_timer
def heap_sort(array):
    """
    堆排序
    :param array:
    :return:
    """

    def build_heap(array, i):
        """
        大顶堆构建
        :param array:
        :param i:
        :return:
        """
        while array[i] > array[(i - 1) // 2] and i > 0:
            array[i], array[(i - 1) // 2] = array[(i - 1) // 2], array[i]
            i = (i - 1) // 2
        return array

    def heapify(array, i, heap_size):
        p = 2 * i + 1
        while p < heap_size:
            if p + 1 < heap_size:
                p = p if array[p] > array[p + 1] else p + 1
            if array[i] < array[p]:
                array[i], array[p] = array[p], array[i]
            else:
                break
            i = p
            p = 2 * i + 1
        return array

    if len(array) < 1:
        return array
    # 建立大顶堆
    for i in range(1, len(array)):
        build_heap(array, i)
    # 不断调整堆顶元素 进行大顶堆重建，并交换最大值至堆最后一个叶子节点
    for j in range(len(array) - 1, 0, -1):
        array[0], array[j] = array[j], array[0]
        heapify(array, 0, j)
    return array


@func_timer
def merge_sort(array):
    """
    归并排序
    将待排序的数组分成前后两个部分，再递归的将前半部分数据和后半部分的数据各自归并排序，得到的两部分数据，然后使用merge合并算法
    （算法见代码）将两部分算法合并到一起。 例如：如果N=1；那么只有一个数据要排序，N=2，只需要调用merge函数将前后合并，N=4，...........
    也就是将一个很多数据的数组分成前后两部分，然后不断递归归并排序，再合并，最后返回有序的数组。
    归并排序的时间复杂度：
    归并排序的最好、最坏和平均时间复杂度都是O(nlogn)，而空间复杂度是O(n)，比较次数介于(nlogn)/2和(nlogn)-n+1，赋值操作的次数是(2nlogn)。
    因此可以看出，归并排序算法比较占用内存，但却是效率高且稳定的排序算法。
    :param array:
    :return:
    """

    def merge(array, tmp_array, left_start, right_start, right_end):
        """
        合并函数
        :param array:
        :param tmp_array:
        :param left_start:
        :param right_start:
        :param right_end:
        :return:
        """
        left_end = right_start - 1
        index = left_start
        num_elements = right_end - left_start + 1
        while left_start <= left_end and right_start <= right_end:
            if array[left_start] <= array[right_start]:
                tmp_array[index] = array[left_start]
                index += 1
                left_start += 1
            else:
                tmp_array[index] = array[right_start]
                index += 1
                right_start += 1
        while left_start <= left_end:
            tmp_array[index] = array[left_start]
            index += 1
            left_start += 1
        while right_start <= right_end:
            tmp_array[index] = array[right_start]
            index += 1
            right_start += 1

        for i in range(0, num_elements):
            array[right_end] = tmp_array[right_end]
            right_end -= 1
        return array

    def merge_s(array, tmp_array, left, right):
        """
        中分
        :param array:
        :param tmp_array:
        :param left:
        :param right:
        :return:
        """
        if left < right:
            center = (right - left) // 2 + left
            merge_s(array, tmp_array, left, center)
            merge_s(array, tmp_array, center + 1, right)
            merge(array, tmp_array, left, center + 1, right)
        return array

    if len(array) < 1:
        return array
    start = 0
    end = len(array) - 1
    tmp_array = [0] * len(array)
    array = merge_s(array, tmp_array, start, end)
    return array


@func_timer
def quick_sort(array):
    """
    快速排序
     * 选择中枢，一般选择第一个或者最后一个元素。本案例，选择第一个元素作为中枢
     * 两个方向，左边的i下标一直往右走，当a[i] <= a[center_index]，
     * 其中center_index是中枢元素的数组下标，而右边的j下标一直往左走，当a[j] > a[center_index]
     * 如果i和j都走不动了，i <= j, 交换a[i]和a[j],重复上面的过程，直到i>j
     * 交换a[j]和a[center_index]，完成一趟快速排序
     * 枢轴采用三数中值分割法可以优化
    :param array:
    :return:
    """

    def q_sort(array, low, high):
        """
        递归排序，利用两路划分
        :param array:
        :param low:
        :param high:
        :return:
        """
        if low < high:
            pivot = partition(array, low, high)
            q_sort(array, low, pivot)
            q_sort(array, pivot + 1, high)
        return array

    def partition(array, low, high):
        """
        实现三数中值分割法
        :param array:
        :param low:
        :param high:
        :return:
        """
        pivot_key = array[low]  # 取第一个
        while low < high:
            # 将比枢轴记录小的交换到低端
            while low < high and array[high] >= pivot_key:
                high -= 1
            array[low] = array[high]
            # 将比枢轴记录大的交换到高端
            while low < high and array[low] <= pivot_key:
                low += 1
            array[high] = array[low]
        # 枢纽所在位置赋值
        array[low] = pivot_key
        # 返回枢纽所在的位置
        return low

    if len(array) < 1:
        return array
    low = 0
    high = len(array) - 1
    q_sort(array, low, high)
    return array


@func_timer
def bucket_sort(array):
    """
    桶排序
    :param array:
    :return:
    """

    def bucket_s(array, min, max):
        buckets = [0] * (max - min + 1)
        # 计算每个元素在序列出现的次数
        for i in range(0, len(array)):
            buckets[array[i] - min] += 1
        # 根据buckets数组中的信息将待排序列的各元素放入相应位置
        index = 0
        for i in range(0, max - min + 1):
            count = buckets[i]
            while count > 0:
                array[index] = i + min
                index += 1
                count -= 1
        return array

    if len(array) < 1:
        return array
    max_value = array[0]
    min_value = array[0]
    for i in range(0, len(array)):
        if array[i] < min_value:
            min_value = array[i]
        if array[i] > max_value:
            max_value = array[i]
    array = bucket_s(array, min_value, max_value)
    return array


if __name__ == '__main__':
    array = [3, 54, 18, 14, 42, 111, 67, 6, 19, 100]
    import numpy as np
    # array = list(np.random.randint(0, 100000, 1000000))
    array_1 = array.copy()
    array_2 = array.copy()
    array_3 = array.copy()
    array_4 = array.copy()
    array_5 = array.copy()
    array_6 = array.copy()
    array_7 = array.copy()
    array_8 = array.copy()
    # print(insertion_sort(array_1))
    # print(bubble_sort(array_2))
    # print(select_sort(array_3))
    # print(shell_sort(array_4))
    print(heap_sort(array_5))
    # print(merge_sort(array_6))
    # print(quick_sort(array_7))
    # print(bucket_sort(array_8))

    # insertion_sort(array_1)
    # bubble_sort(array_2)
    # select_sort(array_3)
    # shell_sort(array_4)
    # heap_sort(array_5)
    # merge_sort(array_6)
    # quick_sort(array_7)
    # bucket_sort(array_8)

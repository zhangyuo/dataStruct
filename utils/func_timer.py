#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-01-22 15:57
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : func_timer.py
# @Software : PyCharm
# @Desc     :
"""

import datetime


def func_timer(func):
    def compute_time(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        total_time = (end_time - start_time).total_seconds()
        print(f'\n{func.__name__}函数共计执行{total_time}秒')
        return result

    return compute_time

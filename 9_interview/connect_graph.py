#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2020-02-05 17:24
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : test2.py
# @Software : PyCharm
# @Desc     : 字节面试-连通图：把所有被0包围的1转化为0
"""

L=[
    [0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1],
    [0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,0],
    [1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0]]

Points=[]
I=len(L)
J=len(L[0])



def connect(i,j):
    if L[i][j]==0:
        L[i][j]=3
        group.append((i,j))
        if i>0:
            if L[i-1][j]==0:
                connect(i-1,j)
        if i<I-1:
            if L[i+1][j]==0:
                connect(i+1,j)
        if j>0:
            if L[i][j-1]==0:
                connect(i,j-1)
        if j<J-1:
            if L[i][j+1]==0:
                connect(i,j+1)

Groups=[]
for i in range(I):
    for j in range(J):
        group=[]
        if L[i][j]==0:
            connect(i,j)
        if group:
            Groups.append(group[:])
result=[]
for eachgroup in Groups:
    for each in eachgroup:
        if not each[0] or not each[1] or each[0]==I-1 or each[1]==J-1:
            break
    else:
        result.append(len(eachgroup))
print(result)

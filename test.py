#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2021-04-22 09:53
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : test.py
# @Software : PyCharm
# @Desc     :
"""

import sys

print('input A file path:', sys.argv[1])
print('input B file path:', sys.argv[2])

a_path = sys.argv[1]
b_path = sys.argv[2]
# a_path = "./A.txt"
# b_path = "./B.txt"

# read file
match_items = []
with open(b_path, "r", encoding="utf-8") as fr:
    lines = fr.readlines()
    for line in lines:
        line = line.strip().split("\t")
        if len(line) == 2:
            if line[0] == "Protein names" and line[1] == "Gene names":
                continue
            match_items.append((line[0], line[1]))

key_items = []
with open(a_path, "r", encoding="utf-8") as fr:
    lines = fr.readlines()
    for line in lines:
        line = line.strip()
        if line == "protein name":
            continue
        key_items.append(line)

# match name
result = {}
for key in key_items:
    gene_name_list = []
    for match_item in match_items:
        protein_name = match_item[0]
        gene_name = match_item[1]
        if key == protein_name or key in protein_name:
            gene_name_list.append(gene_name)
    result[key] = gene_name_list

# output result
with open("./result.csv", "w", encoding="gbk") as fw:
    for key, name in result.items():
        # name_list = ",".join(name)
        name_list = str(name).replace(",", "，")
        key = key.replace(",", "，")
        line = "%s,%s\n" % (key, name_list)
        fw.write(line)

print("result file save success!")

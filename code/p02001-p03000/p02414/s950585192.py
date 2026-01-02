# -*- coding: utf-8 -*-

import sys
import os


def input_to_list():
    return list(map(int, input().split()))

def get_column(M, i):
    lst = []
    for row in M:
        lst.append(row[i])
    return lst

def dot(lst0, lst1):
    if len(lst0) != len(lst1):
        print('error')
    else:
        s = 0
        for i in range(len(lst0)):
            s += lst0[i] * lst1[i]
        return s

n, m, l = input_to_list()

A = []
for i in range(n):
    A.append(input_to_list())

B = []
for i in range(m):
    B.append(input_to_list())

C = []
for i in range(n):
    C_row = []
    for j in range(l):
        row = A[i]
        col = get_column(B, j)
        C_row.append(dot(row, col))
    C.append(C_row)

# print
for row in C:
    print(*row)
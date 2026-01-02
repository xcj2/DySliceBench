#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	stable_sort
# CreatedDate:  2020-07-08 14:29:32 +0900
# LastModified: 2020-07-08 14:56:46 +0900
#


import os
import sys
from copy import deepcopy
# import numpy as np
# import pandas as pd


def BubbleSort(a, n):
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1][1] > a[j][1]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp


def SelectionSort(b, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if b[j][1] < b[minj][1]:
                minj = j
        tmp = b[minj]
        b[minj] = b[i]
        b[i] = tmp



def main():
    n = int(input())
    s = list(map(str, input().split()))
    a = deepcopy(s)
    b = deepcopy(s)
    BubbleSort(a, n)
    print(a[0], end='')
    for i in range(1, n):
        print(" {}".format(a[i]), end='')
    print()
    print("Stable")

    SelectionSort(b, n)
    print(b[0], end='')
    for i in range(1, n):
        print(" {}".format(b[i]), end='')
    print()
    for a_, b_ in zip(a, b):
        if a_!=b_:
            print("Not stable")
            return
    print("Stable")


if __name__ == "__main__":
    main()


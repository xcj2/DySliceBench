def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

A, B, M = getNM()
# それぞれ冷蔵庫の値段
ref_a = getList()
ref_b = getList()
# 一枚だけ使える
ticket = [getList() for i in range(M)]

ans = min(ref_a) + min(ref_b)
for i in ticket:
    opt = ref_a[i[0] - 1] + ref_b[i[1] - 1] - i[2]
    ans = min(ans, opt)
print(ans)
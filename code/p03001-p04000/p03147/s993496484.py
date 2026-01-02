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
import copy
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N = getN()
H = getList()
now = H[0]
ans = 0
for i in range(1, N):
    if now <= H[i]:
        now = H[i]
    else:
        ans += H[i - 1] - H[i]
        now = H[i]
ans += H[-1]
print(ans)
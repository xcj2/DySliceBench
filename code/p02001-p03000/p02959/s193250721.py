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
A = getList()
B = getList()
cnt = 0
for i in range(N):
    minus1 = min(A[-i - 1], B[-i - 1])
    A[-i - 1] -= minus1
    B[-i - 1] -= minus1
    cnt += minus1
    minus2 = min(A[-i - 2], B[-i - 1])
    A[-i - 2] -= minus2
    B[-i - 1] -= minus2
    cnt += minus2
print(cnt)
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

N = getN()
P = getList()

cnt = 0
for i in range(N - 1):
    now = P[i]
    next = P[i + 1]
    if i + 1 == now:
        P[i] = next
        P[i + 1] = now
        cnt += 1
if P[-1] == N:
    print(cnt + 1)
else:
    print(cnt)

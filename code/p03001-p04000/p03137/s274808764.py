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

N, M = getNM()
X = getList()
X. sort()
Xalta = []
for i in range(M - 1):
    Xalta.append(-1 * abs(X[i + 1] - X[i]))
heapq.heapify(Xalta)

for i in range(N - 1):
    if len(Xalta) > 0:
        heapq.heappop(Xalta)
print(sum(Xalta) * -1)
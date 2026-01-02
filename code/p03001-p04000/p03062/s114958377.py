def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

N = getN()
A = getList()
alta = []
cntminus = 0
for i in A:
    if i < 0:
        cntminus += 1
    alta.append(abs(i))
if cntminus % 2 == 0:
    print(sum(alta))
else:
    print(sum(alta) - 2 * min(alta))

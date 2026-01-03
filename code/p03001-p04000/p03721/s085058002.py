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

N, K = getNM()
parent = []
for i in range(N):
    a, b = getNM()
    parent.append((a, b))
parent.sort(key = lambda int: int[0])

A = []
B = []
for a, b in parent:
    A.append(a)
    B.append(b)
alta = [0]
for i in range(N):
    alta.append(alta[i] + B[i])

index = bisect_left(alta, K)
print(A[index - 1])

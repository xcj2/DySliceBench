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

from itertools import permutations
from math import factorial, hypot

N, K = getNM()
A = getList()
mi = min(A)
miindex = []
for i in range(N):
    if A[i] == mi:
        miindex.append(i)
ans = 1000000
for i in miindex:
    rang = K - 1
    opt1 = (i + rang - 1) // rang
    newi = opt1 * rang + 1
    opt2 = ((N - newi) + rang - 1) // rang
    ans = min(ans, opt1 + opt2)
print(ans)
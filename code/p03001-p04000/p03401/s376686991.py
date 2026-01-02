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
A = [0] + getList() + [0]

# dp[i + 1] i番目まで抜かさずに行った時の距離の合計
dp = [0]
sta = A[0]
for i in range(1, N + 2):
    dist = abs(A[i] - sta)
    dp.append(dp[-1] + dist)
    sta = A[i]
for i in range(N):
    opt1 = dp[i]
    opt2 = abs(A[i + 2] - A[i])
    opt3 = dp[-1] - dp[i + 2]
    print(opt1 + opt2 + opt3)


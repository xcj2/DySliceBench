# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
from itertools import accumulate
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def floor(a, b): return -(-a // b)


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


def is_kaibun(kaibun):
    for i in range(len(kaibun)//2):
        if kaibun[i] != kaibun[-i-1]:
            return False
    return True


N, M = zz()
next1, next2, next3, next4, next5, next6, next7, next8 = 0, 0, 0, 0, 0, 0, 0, 0
if (N == 1 and M == 1):
    print(1)
    exit()
elif (N == 1 or M == 1):
    next1 = 2
    next2 = (N*M)-2
elif (M == 2 or N == 2):
    next3 = 4
    next5 = (N*M)-4

else:
    next1 = 0
    next2 = 0
    next3 = 4
    next4 = 0
    next5 = (M-2)*2 + (N-2)*2
    next6 = 0
    next8 = (N-2)*(M-2)

# print(next1+next2 + next3 + next4 + next5 + next6 + next7+next8, N*M)
print(next2 + next4 + next6 + next8)

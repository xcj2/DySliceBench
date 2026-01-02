# -*- coding: utf-8 -*-
import math
from operator import mul
from functools import reduce
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


s = S()
t = S()
S = s
T = t

min_ = 0
max_ = len(T)
# len(S) - len(T) + 1
for x in range(max_+1):
    # x文字置き換えて良い
    for i in range(len(S) - len(T) + 1):
        count = 0
        for (a, b) in zip(T, S[i:i + len(T)]):
            if (a == b):
                count += 1
        if (count+x >= len(T)):
            print(x)
            exit()

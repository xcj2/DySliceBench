from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import copy
import time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7


def inp(): return int(sys.stdin.readline())


def inpl(): return list(map(int, sys.stdin.readline().split()))


def inpl_str(): return list(sys.stdin.readline().split())


N = inp()
aa = inpl()

cnts = [0]*(N+10)

for a in aa:
    cnts[a] += 1

S = 0
for a in aa:
    S += cnts[a]-1

S //= 2

for a in aa:
    print(S - cnts[a] + 1)

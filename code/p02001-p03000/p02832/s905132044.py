from collections import defaultdict, deque
import sys
import heapq
import bisect
import itertools
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

def inpl_strl(): return list(sys.stdin.readline())

n = inp()
s = inpl()
b = 1
if s.count(1) == 0:
    print(-1)
else:
    for i in range(n):
        if s[i] == b:
            b += 1
    print(n-(b-1))
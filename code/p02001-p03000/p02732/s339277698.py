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

N = inp()
lis = inpl()
counts = [0]*(N+10)
for i in lis:
    counts[i] += 1

S = 0
for i in lis:
    S += counts[i] - 1

S //= 2

for i in lis:
    print(S - counts[i] + 1)
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

a, b = inpl()
for i in range(10000):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        print(i)
        exit()
print(-1)
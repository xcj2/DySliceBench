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

n, m = inpl()
A = [input() for i in range(n)]
B = [input() for i in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        A1 = [a[j:j+m] for a in A[i:i+m]]
        if A1 == B:
            print('Yes')
            exit()
print('No')
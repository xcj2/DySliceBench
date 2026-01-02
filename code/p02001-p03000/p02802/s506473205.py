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
l = [1] * n
a = 0
q = 0
for i in range(m):
    p, s = inpl_str()
    p = int(p)
    if l[p-1] > 0:
        if  s == 'AC':
            q += l[p-1]-1
            l[p-1] = 0
            a+=1
        else:
            l[p-1]+=1
print(a, q)
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

n = inp()

# 2 3 1
L = inpl()

#1 2 3 
Lsort = sorted(L)

#(2,1) (3,2) (1,3)
zL = list(zip(L, Lsort))

zL.sort(key = lambda x: x[0])
ansL = [_[1] for _ in zL] 
print(' '.join(map(str, ansL)))
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

def pair(n):
    return n*(n-1) // 2

n = inp()
tempcons = 0
ans = 0

Slist = sorted([sorted(input()) for i in range(n)])
for i in range(n-1):
    if Slist[i] == Slist[i+1]:
        tempcons += 1
    else:
        ans += pair(tempcons+1)
        tempcons = 0
ans += pair(tempcons+1)

print(ans)
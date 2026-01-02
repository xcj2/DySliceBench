from collections import defaultdict,deque
import numpy as np
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N,D = inpl()
xx = [inpl() for _ in range(N)]

db = [i**2 for i in range(1,500)]

def dist(i,j):
    tmp = 0
    for k in range(D):
        tmp += (xx[i][k]-xx[j][k])**2
    return tmp

ans = 0
for i in range(N):
    for j in range(i+1,N):
        tmp = dist(i,j)
        if tmp in db:
            ans += 1
print(ans)

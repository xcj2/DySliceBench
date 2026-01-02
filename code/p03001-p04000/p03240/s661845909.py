import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

n = INT()

x = []
y = []
h = []
for i in range(n):
    xx,yy,hh = MAP()
    x.append(xx)
    y.append(yy)
    h.append(hh)

kk = h.index(max(h))
k = 0

for i in range(101):
    for j in range(101):
        ass = h[kk] + abs(x[kk]-i) + abs(y[kk]-j)
        for r in range(n):
            if h[r]==0:
                if ass-abs(x[r]-i)-abs(y[r]-j)>0:
                    ass = -1
                    break
            else:
                if ass != abs(x[r]-i)+abs(y[r]-j)+h[r]:
                    ass = -1
                    break
        if ass!=-1:
            print(i,j,ass)
            break

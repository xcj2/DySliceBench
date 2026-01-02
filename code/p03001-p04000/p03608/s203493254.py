import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))



n,m,r=mp()
l=lmp()
d = [[float("inf")]*(n+1) for i in range(n+1)] 
for i in range(m):
    x,y,z = map(int,input().split())
    d[x][y] = z
    d[y][x] = z
for i in range(n+1):
    d[i][i] = 0
for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])

lis=list(itertools.permutations(l))
ans=float("inf")
for k in range(len(lis)):
    c=0
    for i in range(r-1):
        c+=d[lis[k][i]][lis[k][i+1]]
    ans=min(ans,c)
print(ans)
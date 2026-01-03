import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from heapq import heappop, heappush
def dijkstra(E,s,n,inf=float('inf')):
    d = [inf]*n
    d[s] = 0
    q = []
    heappush(q,(0,s))
    while q:
        du,u = heappop(q)
        if d[u] < du:
            continue
        for v,dist in E[u]:
            dnew = du + dist
            if d[v] > dnew:
                d[v] = dnew
                heappush(q,(dnew,v))
    return d

N = I()
a,b,c = LIR(N-1,3)
Q,K = LI()
x,y = LIR(Q,2)

E = [[] for _ in range(N)]
for i in range(N-1):
    E[a[i]-1].append((b[i]-1,c[i]))
    E[b[i]-1].append((a[i]-1,c[i]))

d = dijkstra(E,K-1,N,inf=10**9*(N-1)+1)

for i in range(Q):
    print(d[x[i]-1]+d[y[i]-1])
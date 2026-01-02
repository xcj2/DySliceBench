import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,M = II()
L,R,C = Line(M,3)

from heapq import heappop, heappush
def dijkstra(E,s,n):
    inf=float('inf')
    d=[inf for _ in range(n)]
    d[s]=0
    q=[]
    heappush(q,(0,s))
    while q:
        du, u1 = heappop(q)
        if d[u1]<du: continue
        for v1,weight in E[u1].items():
            alt=du+weight
            if d[v1]>alt:
                d[v1]=alt
                heappush(q, (alt,v1))
    return d

A = []
for i in range(M):
    A.append((L[i]-1,R[i]-1,C[i]))
A.sort(key=lambda x:-x[2])

E = [dict() for _ in range(N)]
for i in range(M):
    E[A[i][0]][A[i][1]] = A[i][2]

for i in range(N-1):
    E[i+1][i] = 0

d = dijkstra(E,0,N)
if d[-1]==float('inf'):
    print(-1)
else:
    print(d[-1])
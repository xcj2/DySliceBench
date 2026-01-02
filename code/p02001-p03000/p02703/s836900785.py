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

N,M,S = LI()
U,V,A,B = LIR(M,4)
C,D = LIR(N,2)

max_ = (N-1)*max(A)
E = [dict() for _ in range(N*(max_+1))]

def number(i,j):
    return i*(max_+1)+j

def dijkstra(E,s,n):
    d = [10**9*(max_+1)*N]*n
    d[s] = 0
    q = []
    heappush(q,(0,s))
    while q:
        du,u = heappop(q)
        if d[u] < du:
            continue
        for v,weight in E[u].items():
            dnew = du + weight
            if d[v] > dnew:
                d[v] = dnew
                heappush(q,(dnew,v))
    return d

for i in range(N):
    for j in range(max_-C[i]+1):
        E[number(i,j)][number(i,j+C[i])] = D[i]

for i in range(M):
    for j in range(A[i],max_+1):
        E[number(U[i]-1,j)][number(V[i]-1,j-A[i])] = B[i]
        E[number(V[i]-1,j)][number(U[i]-1,j-A[i])] = B[i]

d = dijkstra(E,min(S,max_),N*(max_+1))

for i in range(1,N):
    ans = float('inf')
    for j in range(max_+1):
        if d[number(i,j)] < ans:
            ans = d[number(i,j)]
    print(ans)
#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

def BF(E,s,n):
    inf=float("inf")
    d=[inf for _ in range(n)]
    d[s]=0
    for i in range(2*n):
        for e in E:
            if d[e[0]]!=inf and d[e[1]]>d[e[0]]+e[2]:
                d[e[1]] = d[e[0]] + e[2]
                if i>=n:
                    d[e[1]] = -float('inf')
    return d

N,M,P = II()
A,B,C = Line(M)
E = []
for i in range(M):
    E.append([A[i]-1, B[i]-1, -C[i]+P])

d = BF(E,0,N)
if d[N-1]==-float('inf'):
    print(-1)
else:
    print(max(0,-d[N-1]))
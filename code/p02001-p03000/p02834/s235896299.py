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

N,u,v = II()
A,B = Line(N-1,2)

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

def bfs(pt,v):
    n = len(pt)
    d = [-1]*n
    d[v] = 0
    q = [v]
    c = 1
    while q:
        q1 = []
        for i in q:
            for j in pt[i]:
                if d[j]==-1:
                    d[j] = c
                    q1.append(j)
        q = q1
        c += 1
    return d

pt = edges_to_pt(A,B,N)
du = bfs(pt,u-1)
dv = bfs(pt,v-1)

ans = 0
for i in range(N):
    if du[i]>=dv[i]:
        continue
    elif len(pt[i])>=2:
        continue
    else:
        ans = max(ans,dv[i]-1)

print(ans)
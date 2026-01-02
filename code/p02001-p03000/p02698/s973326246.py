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

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if not directed:
            pt[t[i]-1].append(s[i]-1)
    return pt

def euler_tour(pt,N,root):
    S = [(~root,-1),(root,-1)]
    tour = [None]*(2*N)  #ツアー順（2*N-1要素）
    F = [None]*N         #最初の到達時刻
    depth = [0]*N
    count = -1
    while(S):
        v,p = S.pop()
        count += 1
        if v >= 0:
            tour[count] = v
            if not F[v]:
                F[v] = count
            for nv in pt[v][::-1]:
                if nv == p:
                    continue
                depth[nv] = depth[v]+1
                S.append((~nv,v))
                S.append((nv,v))
        else:
            tour[count] = p
    tour.pop()
    return tour

N = I()
a = LI()
u,v = LIR(N-1,2)

pt = edges_to_pt(u,v,N)
tour = euler_tour(pt,N,0)

inf = 10**9+1
dp = [inf]*N
record = []
visited = [False]*N
ans = [0]*N
for v in tour:
    if visited[v]:
        r = record.pop()
        dp[r[0]] = r[1]
    else:
        p = bisect_left(dp,a[v])
        record.append((p,dp[p]))
        dp[p] = a[v]
        pinf = bisect_left(dp,inf)
        ans[v] = pinf
        visited[v] = True

for a in ans:
    print(a)
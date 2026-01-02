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

def shortest_path(pt,s,t):
    n = len(pt)
    used = [False]*n
    pre = [-1]*n
    q = [s]
    while q:
        q1 = []
        for i in q:
            for j in pt[i]:
                if not used[j]:
                    used[j] = True
                    pre[j] = i
                    q1.append(j)
        q = q1

    if used[t]:
        path = [t]
        p = t
        while True:
            p = pre[p]
            path.append(p)
            if p == s:
                break
        return list(reversed(path))
    else:
        return []

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

N,M = II()
A,B = Line(M,2)

use_path = []
pt = edges_to_pt(A,B,N,True)
l = N+1
for i in range(N):
    s = shortest_path(pt,i,i)
    if s:
        s.pop()
        if len(s)<l:
            use_path = s
            l = len(s)

if use_path:
    print(len(use_path))
    for v in use_path:
        print(v+1)
else:
    print(-1)
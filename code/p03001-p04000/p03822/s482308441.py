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

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

N = I()
a = Line(N-1,1)

s = [0]*(N-1)
t = [0]*(N-1)
for i in range(N-1):
    s[i] = a[i]
    t[i] = i+2

pt = edges_to_pt(s,t,N,True)
d = bfs(pt,0)
dmax = max(d)

v = [[] for _ in range(dmax+1)]
for i,d1 in enumerate(d):
    v[d1].append(i)

val = [0]*N
level = dmax-1
while level>=0:
    for v1 in v[level]:
        child_val_list = []
        for child in pt[v1]:
            child_val_list.append(val[child])
        if child_val_list:
            child_val_list.sort(reverse=True)
            val[v1] = max([x+(i+1) for i,x in enumerate(child_val_list)])
    level -= 1

print(val[0])
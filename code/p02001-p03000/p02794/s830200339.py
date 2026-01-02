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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

from itertools import product

N = I()
a,b = Line(N-1,2)
M = I()
u,v = Line(M,2)

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

#木の最短パス
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

d = defaultdict(int)
count = 0
for i in range(N-1):
    x,y = min(a[i]-1,b[i]-1),max(a[i]-1,b[i]-1) 
    if not d[(x,y)]:
        d[(x,y)] = count
        d[(y,x)] = count
        count += 1

pt = edges_to_pt(a,b,N)
h_index = [[] for _ in range(M)]
for i in range(M):
    p = shortest_path(pt,u[i]-1,v[i]-1)
    for j in range(len(p)-1):
        x,y = p[j],p[j+1]
        h_index[i].append(d[(x,y)])

bit_h = [0]*M
for i in range(M):
    bits = 0
    for h in h_index[i]:
        bits += 2**h
    bit_h[i] = bits

ans_r = 0
A = list(product([0,1],repeat=M))
for a in A[1:]:
    bits = 0
    edge_num = 0
    for i in range(M):
        if a[i]:
            bits |= bit_h[i]
            edge_num += 1
    one_count = 0
    for i in range(count+1):
        if bits>>i&1:
            one_count += 1
    ans_r += (-1)**(edge_num-1)*2**(N-1-one_count)

print(2**(N-1)-ans_r)
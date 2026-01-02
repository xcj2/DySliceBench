# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = map(int, readline().split())

M = 2*10**5+2
Uy = [[] for _ in range(M)]
Dy = [[] for _ in range(M)]

Rx = [[] for _ in range(M)]
Lx = [[] for _ in range(M)]

d1U = {} # 右上、x+y UR
d1R = {} # 右上、x+y UR
d2U = {} # 左上、x-y UL
d2L = {} # 左上、x-y UL
d3L = {} # 左下、x+y LD
d3D = {} # 左下、x+y LD
d4D = {} # 右下、x-y DR
d4R = {} # 右下、x-y DR

for _ in range(n):
    x,y,z = readline().split()
    x = int(x); y = int(y)
    if z=="U":
        Uy[x].append(y)
        dp,dn = d1U,d2U
    elif z=="D":
        Dy[x].append(y)
        dp,dn = d3D,d4D
    elif z=="R":
        Rx[y].append(x)
        dp,dn = d1R,d4R
    elif z=="L":
        Lx[y].append(x)
        dp,dn = d3L,d2L
    
    v = x+y
    if v in dp: dp[v].append(x)
    else: dp[v] = [x]
    v = x-y
    if v in dn: dn[v].append(x)
    else: dn[v] = [x]

def get(a,b):
    v = INF
    lb = len(b)
    j = 0
    for ai in a:
        while j < lb and b[j] < ai:
            j += 1
        if j < lb:
            v = min(v,b[j]-ai)
    return v

def syoumen(lst1,lst2):
    v = INF
    for i in range(M):
        if lst1[i] and lst2[i]:
            lst1[i].sort()
            lst2[i].sort()
            v = min(v,get(lst1[i],lst2[i]))
    return v*5

def naname(d1,d2):
    v = INF
    for i in range(-2*M,2*M):
        if i in d1 and i in d2:
            d1[i].sort()
            d2[i].sort()
            v = min(v,get(d1[i],d2[i]))
    return v*10

INF = 1<<30
ans = INF

ans = min(ans,syoumen(Uy,Dy))
ans = min(ans,syoumen(Rx,Lx))

ans = min(ans,naname(d1R,d1U))
ans = min(ans,naname(d2U,d2L))
ans = min(ans,naname(d3D,d3L))
ans = min(ans,naname(d4R,d4D))

if ans == INF:
    print("SAFE")
else:
    print(ans)


import math
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

N,M = LI()
AB = [LI() for _ in range(M)]

ans = 0

par = [0]*N
# rank = [0]*N

def init(n):
    for i in range(n):
        # 親のID or 属する頂点の数
        par[i]=-1
        # rank[i] = 0

# rootを返す
def find(x):
    # 根
    if par[x] < 0:
        return x
    # 節の親
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    if (x==y):
        return
    if (par[x] > par[y]):
        x,y = y,x
    # rootの頂点数を結合
    par[x] += par[y]
    # yの親をxに
    par[y] = x
    return

    # if (rank[x]<rank[y]):
    #     par[x]=y
    # else:
    #     par[y]=x
    #     if rank[x] == rank[y]:
    #         rank[x] += 1

def same(x,y):
    return find(x)==find(y)

def size(x):
    return -par[find(x)]

init(N)

for r in AB:
    f = r[0]-1
    t = r[1]-1
    unite(f,t)
    # print(par)

for i in range(N):
    # print(size(i))
    ans = max(ans,size(i))

print(ans)
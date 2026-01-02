from operator import itemgetter
from itertools import *
from bisect import *
from collections import *
from heapq import *
import sys

sys.setrecursionlimit(10**6)

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def SI(): return sys.stdin.readline()[:-1]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
int1 = lambda x: int(x)-1
def MI1(): return map(int1, sys.stdin.readline().split())
def LI1(): return list(map(int1, sys.stdin.readline().split()))
p2D = lambda x: print(*x, sep="\n")
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def SCC(to, ot):
    n = len(to)

    def dfs(u):
        for v in to[u]:
            if com[v]: continue
            com[v] = 1
            dfs(v)
        top.append(u)

    top = []
    com = [0]*n
    for u in range(n):
        if com[u]: continue
        com[u] = 1
        dfs(u)

    def rdfs(u, k):
        for v in ot[u]:
            if com[v] != -1: continue
            com[v] = k
            rdfs(v, k)

    com = [-1]*n
    k = 0
    for u in top[::-1]:
        if com[u] != -1: continue
        com[u] = k
        rdfs(u, k)
        k += 1

    return k, com

class TwoSat:
    def __init__(self, n):
        # to[v][u]...頂点uの値がvのときの遷移先と反転の有無
        self.n = n
        self.to = [[] for _ in range(n*2)]
        self.ot = [[] for _ in range(n*2)]
        self.vals = []

    # uがu_val(0 or 1)ならばvはv_val(0 or 1)
    def add_edge(self, u, u_val, v, v_val):
        self.to[u*2+u_val].append(v*2+v_val)
        self.ot[v*2+v_val].append(u*2+u_val)

    # 条件を満たすかどうかをboolで返す。構成はself.valsに入る
    def satisfy(self):
        k, com = SCC(self.to, self.ot)
        for u in range(self.n):
            if com[u*2]==com[u*2+1]:return False
            self.vals.append(com[u*2]<com[u*2+1])
        return True

n, d = MI()
xy = LLI(n)
ts = TwoSat(n)

for i in range(n):
    x1, y1 = xy[i]
    for j in range(i):
        x2, y2 = xy[j]
        if abs(x1-x2) < d:
            ts.add_edge(i, 0, j, 1)
            ts.add_edge(j, 0, i, 1)
        if abs(x1-y2) < d:
            ts.add_edge(i, 0, j, 0)
            ts.add_edge(j, 1, i, 1)
        if abs(y1-x2) < d:
            ts.add_edge(i, 1, j, 1)
            ts.add_edge(j, 0, i, 0)
        if abs(y1-y2) < d:
            ts.add_edge(i, 1, j, 0)
            ts.add_edge(j, 1, i, 0)

if ts.satisfy():
    print("Yes")
    for j,xyi in zip(ts.vals,xy):print(xyi[j])
else:print("No")

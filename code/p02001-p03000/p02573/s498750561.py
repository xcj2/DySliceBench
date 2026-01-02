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

N,M = LI()
A,B = LIR(M,2)

class UF():
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.size = [1]*n

    # x が属する集合の代表値を返す
    def find(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = y = self.find(self.par[x])
            return y

    # x と y の集合を結合する
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            self.par[py] = px
            self.size[px] += self.size[py]
            return

    # x と y が同じ集合に属するか判定する
    def is_same(self,x,y):
        return self.find(x) == self.find(y)

    # x が属する集合の要素数を返す
    def get_size(self,x):
        return self.size[self.find(x)]

uf = UF(N)
for i in range(M):
    uf.union(A[i]-1,B[i]-1)

ans = 0
for i in range(N):
    ans = max(ans,uf.get_size(i))

print(ans)
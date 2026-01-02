import sys
import math
from collections import defaultdict

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

#Union Find
class UF(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.size = [1]*n

    # x が属する集合の代表値を返す
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # x と y の集合を結合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    # x と y が同じ集合に属するか判定する
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    # x が属する集合の要素数を返す
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]

N,M,K = LI()
A,B = LIR(M,2)
C,D = LIR(K,2)

b = defaultdict(set)
t = defaultdict(set)

uf = UF(N)

for i in range(M):
    uf.union(A[i]-1,B[i]-1)
    t[A[i]-1].add(B[i]-1)
    t[B[i]-1].add(A[i]-1)

num = [0]*N
for i in range(K):
    if uf.is_same(C[i]-1, D[i]-1):
        num[C[i]-1] -= 1
        num[D[i]-1] -= 1

ans = []
for i in range(N):
    ans.append(uf.get_size(i)-1-len(t[i])+num[i])
print(*ans)
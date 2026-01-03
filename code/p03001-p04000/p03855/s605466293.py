import math
import sys
import os
from operator import mul
from collections import Counter

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N,K,L = LI()
pq = [LI() for _ in range(K)]
rs = [LI() for _ in range(L)]

road = UnionFind(N)
for r in pq:
    f = r[0]-1
    t = r[1]-1
    road.union(f,t)

rail = UnionFind(N)
for r in rs:
    f = r[0]-1
    t = r[1]-1
    rail.union(f,t)

# ans = [-1]*N
# for i in range(N):
#     if not ans[i]==-1:
#         continue
#     road_set = set(road.members(i))
#     rail_set = set(rail.members(i))
#     group = road_set & rail_set
#     count = len(group)
#     for j in group:
#         ans[j]=count

union_sets=[(road.find(i),rail.find(i)) for i in range(N)]
# (0,1),(0,1),(2,2)
# 共通の親を持つ数をカウント
counts=Counter(union_sets)
# (0,1):2, (2,2):1
ans=[counts[union_set] for union_set in union_sets]

print(*ans)


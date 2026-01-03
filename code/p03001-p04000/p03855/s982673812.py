import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

N, K, L = MAP()

tree_pq = UnionFind(N+1) # N点集合からUnionFind木を作成
tree_rs = UnionFind(N+1)
pq = [LIST() for _ in range(K)]
for p, q in pq:
	tree_pq.union(p, q) # p, qを同じグループに
group_pq = [tree_pq.find(i) for i in range(N+1)]
# print(group_pq)
rs = [LIST() for _ in range(L)]
for r, s in rs:
	tree_rs.union(r, s)
group_rs = [tree_rs.find(i) for i in range(N+1)]
# print(group_rs)

keys = []
dic = {}
pairs = [(group_pq[i], group_rs[i]) for i in range(N+1)]
for i in range(1, N+1):
	pair = (group_pq[i], group_rs[i])
	keys.append(pair)
	if pair in dic:
		dic[pair] += 1
	else:
		dic[pair] = 1

ans = [str(dic[key]) for key in keys]
print(" ".join(ans))
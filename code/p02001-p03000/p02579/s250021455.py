import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math
import copy
# from fractions import gcd

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)


class Uf:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def root(self, x):
        if self.p[x] != x:
            self.p[x] = self.root(self.p[x])

        return self.p[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        u = self.root(x)
        v = self.root(y)

        if u == v: return

        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def count(self, x):
        return self.size[self.root(x)]


h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
A = [input() for i in range(h)]

tree = Uf(h*w)
for i in range(h):
    for j in range(w):
        if A[i][j] == "#":
            continue
        if i > 0 and A[i-1][j] == ".":
            tree.unite(w*i+j, w*(i-1)+j)
        if i < h-1 and A[i+1][j] == ".":
            tree.unite(w*i+j, w*(i+1)+j)
        if j > 0 and A[i][j-1] == ".":
            tree.unite(w*i+j, w*i+(j-1))
        if j < w-1 and A[i][j+1] == ".":
            tree.unite(w*i+j, w*i+(j+1))

# print(tree.p)

par_list = set()
for i in range(h):
    for j in range(w):
        if A[i][j] == ".":
            par_list.add(tree.root(w*i+j))

# print(par_list)

node = dict()
for i, e in enumerate(par_list):
    node[e] = i

# print(node)

edge_list = set()
for i in range(h):
    for j in range(w):
        if A[i][j] == ".":
            for a in range(max(0, i - 2), min(h, i+3)):
                for b in range(max(0, j - 2), min(w, j + 3)):
                    if A[a][b] == "." and tree.root(w*i+j) != tree.root(w*a+b):
                        edge_list.add((node[tree.root(w*i+j)], node[tree.root(w*a+b)]))
                        edge_list.add((node[tree.root(w*a + b)], node[tree.root(w*i + j)]))

start = node[tree.root(w*(ch-1) + cw-1)]
goal = node[tree.root(w*(dh-1) + dw-1)]

g = [[] for i in range(len(node))]
for e in edge_list:
    g[e[0]].append(e[1])

# print(g, start, goal)

que = deque([(start, 0)])
seen = set()
seen.add(start)
while que:
    cur, time = que.popleft()
    if cur == goal:
        print(time)
        exit()
    for nxt in g[cur]:
        if nxt not in seen:
            seen.add(nxt)
            que.append((nxt, time+1))

print(-1)


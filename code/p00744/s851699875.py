import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in range(n)]

    def add_edge(self, fr, to, cap):
        #[to, cap, rev]
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.g[fr].append(forward)
        self.g[to].append(backward)

    def add_bidirectional_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.g[v1].append(edge1)
        self.g[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.n
        deq = deque([s])
        level[s] = 0
        g = self.g
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in g[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**30
        g = self.g
        while self.bfs(s, t):
            self.it = list(map(iter, self.g))
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

ans = []
while 1:
    m, n = MAP()
    if m == 0:
        break
    D = Dinic(m+n+2)
    B = LIST()
    while len(B) < m:
        B += LIST()

    R = LIST()
    while len(R) < n:
        R += LIST()
    s = m+n
    t = s+1

    for i in range(m):
        D.add_edge(s, i, 1)

    for i in range(n):
        D.add_edge(m+i, t, 1)

    for i, x in enumerate(B):
        for j, y in enumerate(R):
            if gcd(x, y) != 1:
                D.add_edge(i, m+j, 1)

    ans.append(D.flow(s, t))
print(*ans, sep="\n")


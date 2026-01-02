from sys import stdin, setrecursionlimit
input = stdin.buffer.readline
setrecursionlimit(10 ** 7)

from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, combinations_with_replacement
from itertools import accumulate
from math import ceil, sqrt, pi, radians, sin, cos

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    def find(self, x):
        y = self.root[x]
        if x == y:
            return x
        else:
            z = self.find(y)
            self.root[x] = z
            return z
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        sx = self.size[rx]
        sy = self.size[ry]
        if rx == ry:
            return 0
        else:
            if sx >= sy:
                self.root[ry] = rx
                self.size[rx] = sx + sy
            else:
                self.root[rx] = ry
                self.size[ry] = sx + sy
        return sx * sy
    def check(self):
        print([self.find(i) for i in range(1, len(self.root))])

MOD = 10 ** 9 + 7
INF = 10 ** 18

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

uf = UnionFind(N)

for a, b in AB:
    uf.union(a, b)

cnt = [0] * (N + 1)
for i in range(1, N + 1):
    cnt[uf.find(i)] += 1
print(max(cnt))
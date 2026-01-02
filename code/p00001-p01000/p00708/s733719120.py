import heapq
import math
from itertools import combinations


class UnionFind:
    from collections import deque

    def __init__(self, v):
        self.v = v
        self._tree = list(range(v + 1))

    def _root(self, a):
        queue = self.deque()
        while self._tree[a] != a:
            queue.append(a)
            a = self._tree[a]
        while queue:
            index = queue.popleft()
            self._tree[index] = a
        return a

    def union(self, a, b):
        root_a = self._root(a)
        root_b = self._root(b)
        self._tree[root_b] = root_a

    def find(self, a, b):
        return self._root(a) == self._root(b)


while True:
    N = int(input())

    if N == 0:
        break

    V = [tuple(map(float, input().split(' '))) for _ in range(N)]
    E = []
    for i, j in combinations(range(N), r=2):
        xi, yi, zi, ri = V[i]
        xj, yj, zj, rj = V[j]
        d = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2)
        c = max(0.0, d - ri - rj)
        heapq.heappush(E, (c, i, j))

    uf = UnionFind(N)
    cost = 0.0
    while E:
        c, i, j = heapq.heappop(E)
        if not uf.find(i, j):
            uf.union(i, j)
            cost += c

    print('{:.3f}'.format(cost))


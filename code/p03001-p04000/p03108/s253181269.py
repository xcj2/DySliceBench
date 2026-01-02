#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math


class UnionFindTree(object):
    def __init__(self, n):
        import collections
        self.parent = list(range(n))
        self.counts = collections.defaultdict(lambda: 1)
        self.rank = collections.defaultdict(int)

    def root(self, x):
        if x == self.parent[x]:
            return x
        root = self.root(self.parent[x])
        self.parent[x] = root
        return root

    def _merge(self, x, y):
        """
        x to y
        """
        self.parent[x] = y
        self.counts[y] += self.counts[x]
        del (self.counts[x])

    def size(self, x):
        return self.counts[self.root(x)]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self._merge(x, y)
        elif self.rank[x] > self.rank[y]:
            self._merge(y, x)
        else:
            self._merge(x, y)
            self.rank[y] += 1


def combination2(n):
    return int(n * (n - 1) / 2)


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
bridges = []
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split(" "))
    bridges.append([A, B])

results = [combination2(N)]
connections = []

# for A, B in reversed(bridges):
#     iA, iB = -1, -1
#     for i, connection in enumerate(connections):
#         if A in connection:
#             iA = i
#         if B in connection:
#             iB = i
#     if iA == -1:
#         connections.append(set([A]))
#         iA = len(connections) - 1
#     if iB == -1:
#         connections.append(set([B]))
#         iB = len(connections) - 1
#     if iA != iB:
#         connections[iA] = connections[iA] | connections[iB]
#         del (connections[iB])
#
#     count = combination2(N)
#     for connection in connections:
#         count -= combination2(len(connection))
#
#     results.append(count)
#
# for result in reversed(results[:-1]):
#     print(result)

results = [combination2(N)]
union_find_tree = UnionFindTree(N)
for A, B in reversed(bridges):
    if union_find_tree.same(A-1, B-1):
        results.append(results[-1])
    else:
        last_result = results[-1] + combination2(union_find_tree.size(A - 1)) + combination2(
            union_find_tree.size(B - 1))
        union_find_tree.union(A - 1, B - 1)
        results.append(last_result - combination2(union_find_tree.size(A - 1)))

for result in reversed(results[:-1]):
    print(result)

exit(0)

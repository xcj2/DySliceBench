# coding: utf-8

import sys
import math

import array
import bisect
import collections
from collections import Counter, defaultdict
import fractions
import heapq
import re

sys.setrecursionlimit(1000000)


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]

def argsort(l, reverse=False):
    return sorted(range(len(l)), key=lambda i: l[i], reverse=reverse)

def argmin(l):
    return l.index(min(l))

def YESNO(ans, yes="YES", no="NO"):
    print([no, yes][ans])


II = lambda: int(input())
MI = lambda: map(int, input().split())
MIL = lambda: list(MI())
MIS = lambda: input().split()


class UnionFind(object):
    """UnionFind (経路圧縮、ランクあり)"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self._size = [1] * n

    def _set_parent(self, parent, child):
        self._size[parent] = self.size(parent) + self.size(child)
        self.parent[child] = parent

    def size(self, node):
        return self._size[self.root(node)]

    def union(self, n1, n2):
        r1, r2 = self.root(n1), self.root(n2)

        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self._set_parent(r1, r2)
            else:
                self._set_parent(r2, r1)
                if self.rank[r1] == self.rank[r2]:
                    self.rank[r1] += 1

    def root(self, node):
        p = self.parent[node]
        if p == node:
            return p
        p = self.root(p)
        self.parent[node] = p
        return p

    def same(self, n1, n2):
        return self.root(n1) == self.root(n2)


def main():
    N, M = MI()
    bridges = []
    for i in range(M):
        a, b = MI()
        bridges.append((a-1, b-1))

    costs = [N * (N-1) // 2]
    uf = UnionFind(N)
    for a, b in bridges[::-1]:
        if uf.same(a, b):
            costs.append(costs[-1])
        else:
            costs.append(costs[-1] - uf.size(a) * uf.size(b))
        uf.union(a, b)
    for c in costs[-2::-1]:
        print(c)


if __name__ == "__main__":
    main()

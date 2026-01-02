#!/usr/bin/env python3

import sys
from collections import namedtuple

DEBUG = False


def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep=" "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


Point = namedtuple("Point", ("id", "to"))
points = {}


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


def scc_forward(p, visited, rev_scc_ponints):
    if p in visited:
        return
    visited.add(p)
    for to in points[p].to:
        scc_forward(to, visited, rev_scc_ponints)
    rev_scc_ponints.append(p)


def scc_backword(p, visited, cur_sc):
    if p in visited:
        return 0
    visited.add(p)
    cur_sc.add(p)
    for to in points[p].to:
        scc_backword(to, visited, cur_sc)
    print(repr(cur_sc))
    return len(cur_sc)


def count_max_sc_size(points):
    rev_scc_points = []
    visited_forward = set()
    for p in points:
        scc_forward(p, visited_forward, rev_scc_points)

    max_sc_size = 1
    visited_backward = set()
    for p in rev_scc_points:
        cur_sc_size = scc_backword(p, visited_backward, set())
        if cur_sc_size > max_sc_size:
            max_sc_size = cur_sc_size
    return max_sc_size


def old_main():
    _n, m = read_list(int)
    for _ in range(0, m):
        a, b = read_list(int)
        a -= 1
        b -= 1

        if a not in points:
            points[a] = Point(a, set())
        if b not in points:
            points[b] = Point(b, set())
        f = points[a]
        t = points[b]
        f.to.add(b)
        t.to.add(a)
    print(count_max_sc_size(points))


def main():
    n, m = read_list(int)
    union_find = UnionFind(n)
    for _ in range(0, m):
        a, b = read_list(int)
        a -= 1
        b -= 1
        union_find.union(a, b)

    max_size = 1
    for i in range(0, n):
        if union_find.size(i) > max_size:
            max_size = union_find.size(i)
    print(max_size)


if __name__ == "__main__":
    main()

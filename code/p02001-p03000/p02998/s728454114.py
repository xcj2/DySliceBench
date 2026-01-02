#!/usr/bin/env python3
import sys
from itertools import product
sys.setrecursionlimit(10**8)


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


def compress(X, Y):
    dx = list(sorted(set(X)))
    dx_inv = {x: i for i, x in enumerate(dx)}
    dy = list(sorted(set(Y)))
    dy_inv = {y: i for i, y in enumerate(dy)}
    return (dx, dy), (dx_inv, dy_inv)


def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    (decx, decy), (encx, ency) = compress(X, Y)

    H = len(decx)
    uf = UnionFind(len(decx) + len(decy))

    for i in range(N):
        x, y = encx[X[i]], ency[Y[i]]+H
        # print(x, y)
        uf.union(x, y)

    dx = {}
    for i in range(len(decx)):
        key = uf.find(i)
        if key not in dx:
            dx[key] = 1
        else:
            dx[key] += 1
    dy = {}
    for i in range(H, H+len(decy)):
        key = uf.find(i)
        if key not in dy:
            dy[key] = 1
        else:
            dy[key] += 1
    # print(dx, dy)
    # print(uf.all_group_members())
    ans = 0
    for key in dx:
        if key in dy:
            ans += dy[key]*dx[key]
    print(ans-N)
    return


if __name__ == '__main__':
    main()

#import math
#import bisect
#import numpy as np
#import itertools
#import copy
#import collections
import sys

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

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    n, m, k = list(map(int,ipti().split()))
    r = UnionFind(n)
    rr = [0] * n
    fr = [[0] * 2 for _ in range(m)]
    bl = [[0] * 2 for _ in range(k)]

    for i in range(m):
        a, b = list(map(int,ipti().split()))
        fr[i][0] = a - 1
        fr[i][1] = b - 1
        r.union(fr[i][0], fr[i][1])

    for i in range(k):
        a, b = list(map(int,ipti().split()))
        bl[i][0] = a - 1
        bl[i][1] = b - 1

    for i in range(m):
        a, b = fr[i][0], fr[i][1]
        if r.same(a, b):
            rr[a] += 1
            rr[b] += 1

    for i in range(k):
        a, b = bl[i][0], bl[i][1]
        if r.same(a, b):
            rr[a] += 1
            rr[b] += 1

    ans = [0] * n

    for i in range(n):
        ans[i] = r.size(i) - rr[i] - 1

    print(*ans)

if __name__ == '__main__':
    main()

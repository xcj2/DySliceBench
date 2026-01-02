import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

# https://note.nkmk.me/python-union-find/

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


def main():
    n, k = ns()
    p = na1()
    c = na()

    uf = UnionFind(n)
    for i, pi in enumerate(p):
        uf.union(i, pi)

    cycledist = [[-INF for _ in range(2)] for __ in range(n)]
    for lis in uf.all_group_members().values():
        tmp = 0
        l = len(lis)
        for idx in lis:
            tmp += c[idx]
            cycledist[idx][1] = l
        for idx in lis:
            cycledist[idx][0] = tmp

    ans = -INF

    for i in range(n):
        flg = k // cycledist[i][1] > 0
        tmp_ans = cycledist[i][0] * ((k // cycledist[i][1]) - 1) if flg else 0

        tmp = 0
        idx = i
        for j in range(cycledist[i][1] * flg + k % cycledist[i][1]):
            tmp += c[p[idx]]
            idx = p[idx]
            ans = max(ans, tmp_ans + tmp)

        tmp = 0
        idx = i
        for j in range(min(k, cycledist[i][1])):
            tmp += c[p[idx]]
            idx = p[idx]
            ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()

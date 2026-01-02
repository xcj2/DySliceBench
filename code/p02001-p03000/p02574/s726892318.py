import sys
import math
import collections
import bisect
import itertools
import decimal

# import numpy as np

# sys.setrecursionlimit(10 ** 6)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===


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
    n = ni()
    a = na()

    tmp = len(a)

    # 素数列挙
    def Eratosthenes(n):  # N以下のすべての値に対して素数を返す
        a = [[] for _ in range(n + 1)]
        if n >= 2:
            for i in range(2, n + 1):
                if len(a[i]) == 0:
                    for j in range(i, n + 1, i):
                        a[j].append(i)
        return a

    l = max(a)
    p = Eratosthenes(l)
    cnt = [0 for _ in range(l + 1)]

    pc = True
    tc = True

    for ai in a:
        for pi in p[ai]:
            cnt[pi] += 1
            if cnt[pi] >1:
                pc = False
            if cnt[pi] == n:
                tc = False
                break


    if pc:
        print("pairwise coprime")
    elif tc:
        print("setwise coprime")
    else:
        print("not coprime")

if __name__ == '__main__':
    main()

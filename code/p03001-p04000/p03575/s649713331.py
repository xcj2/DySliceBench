import sys
import os
import math
import bisect
import collections
import itertools
import heapq
import re
import queue
from decimal import Decimal

# import fractions

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)
# lcm = lambda x, y: (x * y) // fractions.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


class UnionFind:
    def __init__(self, N):
        self.tree = list(range(N))

    def root(self, N):
        if self.tree[N] == N:
            return N
        else:
            self.tree[N] = self.root(self.tree[N])
            return self.tree[N]

    def same(self, x, y):
        return self.root(self.tree[x]) == self.root(self.tree[y])

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            self.tree[x] = y


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, M = il()
    XY = [il() for _ in range(M)]

    ret = 0
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            if i != j:
                x, y = XY[j]
                uf.unite(x - 1, y - 1)
        x, y = XY[i]
        if not uf.same(x - 1, y - 1):
            ret += 1
    print(ret)


if __name__ == '__main__':
    main()

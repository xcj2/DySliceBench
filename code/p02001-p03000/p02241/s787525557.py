import sys, os, math, bisect, itertools, collections, heapq, queue, copy, array

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
INF = float('inf')


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

    N = ii()
    uf = UnionFind(N)
    ret = 0
    cost = []
    for i in range(N):
        D = il()
        for j in range(N):
            if D[j] != -1:
                cost.append((D[j], i, j))
    else:
        cost.sort()
        for c, v1, v2 in cost:
            if not uf.same(v1, v2):
                ret += c
                uf.unite(v1, v2)
        print(ret)


if __name__ == '__main__':
    main()


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

    N, Q = il()
    uf = UnionFind(N)
    for q in range(Q):
        com, x, y = il()
        if com == 0:
            uf.unite(x, y)
        else:
            print(1 if uf.same(x, y) else 0)


if __name__ == '__main__':
    main()


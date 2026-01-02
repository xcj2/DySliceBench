import sys
from itertools import product

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


H, W = il()
S = imi(H, str)
tree = UnionFind(H * W)
for i, j in product(range(H), range(W)):
    for d in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        x = i + d[0]
        y = j + d[1]
        if 0 <= x < H and 0 <= y < W:
            if S[i][j] != S[x][y]:
                tree.union((i * W + j), (x * W + y))

dot = [0] * (H * W)
sharp = [0] * (H * W)
for i, j in product(range(H), range(W)):
    if S[i][j] == ".":
        dot[tree.find(i * W + j)] += 1
    else:
        sharp[tree.find(i * W + j)] += 1

ans = 0
for i in range(H * W):
    ans += dot[i] * sharp[i]
print(ans)
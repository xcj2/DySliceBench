import sys

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
        self.par = [i for i in range(n)]
        self.rank = [0] * (n)

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


def solve():
    H, W = il()
    S = imi(H, str)
    from itertools import product

    dst = ((i, j) for i, j in product(range(-1, 2), repeat=2))
    dst = list(dst)
    B = [[0] * W for _ in range(H)]
    sharp_pos = []
    for i, j in product(range(H), range(W)):
        if S[i][j] == "#":
            B[i][j] = "#"
            sharp_pos.append((i, j))
    for i, j in sharp_pos:
        for d in dst:
            x = i + d[1]
            y = j + d[0]
            if 0 <= x < H and 0 <= y < W:
                if S[i][j] == "#" and S[x][y] == ".":
                    B[x][y] += 1
    for b in B:
        print("".join(map(str, b)))


if __name__ == "__main__":
    solve()

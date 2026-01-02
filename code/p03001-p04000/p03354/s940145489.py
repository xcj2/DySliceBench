import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    class UnionFind:
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        # 親が同じか判別
        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        # 根を繋ぎ直す
        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x == y:
                return
            if self.parents[x] > self.parents[y]:
                x, y = y, x
            self.parents[x] += self.parents[y]
            self.parents[y] = x

        # 親が同じか判別
        def same(self, x, y):
            return self.find(x) == self.find(y)

        # 連結成分の大きさを返す
        def size(self, x):
            return -self.parents[self.find(x)]

    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    uf = UnionFind(n)
    for _ in range(m):
        x, y = map(int, input().split())
        uf.union(x - 1, y - 1)

    idx = [0] * n
    for i in range(n):
        idx[P[i] - 1] = i

    res = 0
    for j in range(n):
        if j + 1 != P[j]:
            if uf.same(j, idx[j]):
                res += 1
        else:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()

#!/usr/bin/env python3
import sys


class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parents[y] = x


def main():
    N, M = map(int, input().split())
    a = [None] * M
    b = [None] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())

    ans = 0
    for i in range(M):
        # a[i], b[i] 以外を使ってUnionFind木を作り
        # グラフ全体が非連結になるなら橋
        uf = UnionFind(N)
        for j in range(M):
            if i != j:
                uf.union(a[j]-1, b[j]-1)

        p = uf.find(0)
        for k in range(1, N):
            if p != uf.find(k):
                ans += 1
                break
    print(ans)


if __name__ == '__main__':
    main()

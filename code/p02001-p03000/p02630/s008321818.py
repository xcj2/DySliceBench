#!/usr/bin/env python3
import sys
from collections import Counter
sys.setrecursionlimit(10**8)
INF = float("inf")


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
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B, C = [0]*Q, [0]*Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    # 個数を持つ
    # Biの個数 O(1),C[i]の個数 O(1) 更新 O(1) 総和O(1)

    group = [None]*(10**5+1)
    uf = UnionFind(N)

    # union_find
    # N個の数に対して、i番目の数がどのグループに属するのかを示す
    # group
    # j (< 10**5)に対して、jがつけられているグループの根の番号を示す

    for i, a in enumerate(A):
        # グループにつけられている番号がaであるようなグループはあるか？
        # なければ自信のグループにつけられている番号として保持
        # あればそこに合流
        if group[a] is None:
            group[a] = i
        else:
            uf.union(i, group[a])
            group[a] = uf.find(i)
    # print(A)
    # print(group)
    # print(uf.parents)

    tot = sum(A)
    for i in range(Q):
        if group[B[i]] is None:
            b = 0
        elif group[C[i]] is None:
            b = uf.size(group[B[i]])
            group[C[i]] = uf.find(group[B[i]])
            group[B[i]] = None
        else:
            b = uf.size(group[B[i]])
            uf.union(group[B[i]], group[C[i]])
            group[C[i]] = uf.find(group[B[i]])
            group[B[i]] = None
        tot = tot - B[i]*b + C[i]*b
        print(tot)
        # print(group)
        # print(uf.parents)

    return


if __name__ == '__main__':
    main()

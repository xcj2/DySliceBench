from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations
import math
import bisect
import numpy as np
from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# MOD = 10 ** 9 + 7
INF = float("inf")


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # 各要素の親要素の番号を格納するリスト

    def find(self, x):  # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # 要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # 要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x):  # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数を返す
        return len(self.roots())

    def all_group_members(self):  # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    N, M, K = map(int, input().split())
    graph_friends =[[] for _ in range(N)]
    uf_friends = UnionFind(N)
    for _ in range(M):
        a, b = [int(i) - 1 for i in input().split()]
        graph_friends[a].append(b)
        graph_friends[b].append(a)
        uf_friends.union(a, b)

    graph_block = [[] for _ in range(N)]
    for _ in range(K):
        c, d = [int(i) - 1 for i in input().split()]
        graph_block[c].append(d)
        graph_block[d].append(c)

    ans = [0] * N
    for i in range(N):
        size = uf_friends.size(i) - 1
        for f in graph_friends[i]:  # 「友達関係」の時は外す
            if uf_friends.same(i, f):  # 隣接して絵いるかつ親が同じ
                size -= 1
        for b in graph_block[i]:  # 「ブラック関係」の時は外す
            if uf_friends.same(i, b):  # 隣接してるかつ親が同じ
                size -= 1
        ans[i] = size
    print(*ans)


if __name__ == '__main__':
    main()

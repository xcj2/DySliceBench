#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")
from collections import defaultdict


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, src, dest, w=1):
        self.E[src].append((dest, w))
        self.E[dest].append((src, w))  # 無向グラフ


class UnionFind(object):
    def __init__(self, N):
        self.tree = list(range(N))

    def root(self, i):
        if self.tree[i] == i:
            return i
        else:
            self.tree[i] = self.root(self.tree[i])
            return self.tree[i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.tree[x] = y


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):

    # ブロック関係
    block = Graph(N)
    for c, d in zip(C, D):
        block.add_edge(c-1, d-1)

    # 友好関係
    friendUF = UnionFind(N)
    degree = [0]*N
    for a, b in zip(A, B):
        friendUF.unite(a-1, b-1)
        degree[a-1] += 1
        degree[b-1] += 1

    # 友好的に連結している数を調べる
    group = defaultdict(int)
    for i in range(N):
        group[friendUF.root(i)] += 1

    ans = []
    for i in range(N):
        # iの連結している個数 - 次数 - 1 （自身を除く）
        # print(" -- {} --".format(i))
        # print(group[friendUF.root(i)], degree[i])
        ans.append(group[friendUF.root(i)] - degree[i] - 1)
        # ブロックを考慮する
        for dest, _ in block.E[i]:
            if friendUF.same(dest, i):
                ans[-1] -= 1
    print(*ans, sep=" ")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, K, A, B, C, D)


if __name__ == '__main__':
    main()

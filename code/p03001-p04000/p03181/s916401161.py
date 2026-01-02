#!/usr/bin/env python3
import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append((t, w))


def solve(N: int, M: int, x: "List[int]", y: "List[int]"):
    g = Graph(N)
    for xx, yy in zip(x, y):
        g.add_edge(xx-1, yy-1)
        g.add_edge(yy-1, xx-1)

    dp = [0]*N

    def dfs(node, par=-1):
        dp[node] = 1
        for child, _ in g.E[node]:
            if child == par:
                continue
            dp[node] *= dfs(child, node) + 1
            dp[node] %= M
        return dp[node]

    ans = [0]*N

    def dfs_2(node, par=-1):
        ans[node] = 1
        for child, _ in g.E[node]:
            ans[node] *= dp[child]+1
            ans[node] %= M

        # 一要素を覗いた積を求めるため、昇順の積、降順の積を求めておく
        K = len(g.E[node])
        left, right = [1]*K, [1]*K
        for i in range(K):
            t, w = g.E[node][i]
            left[i] = left[i-1]*(dp[t]+1)
            left[i] %= M
        for i in range(K-1, -1, -1):
            t, w = g.E[node][i]
            if i != K-1:
                right[i] = right[i+1]*(dp[t]+1)
            else:
                right[i] = dp[t]+1
            right[i] %= M

        for i in range(K):
            child, _ = g.E[node][i]
            if child == par:
                continue
            dp[node] = 1
            if i:
                dp[node] *= left[i-1]
            if i+1 < K:
                dp[node] *= right[i+1]
            dp[node] %= M
            dfs_2(child, node)
    dfs(0)
    dfs_2(0)

    for a in ans:
        print(a % M)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (N - 1)  # type: "List[int]"
    y = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)


if __name__ == '__main__':
    main()

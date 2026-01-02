#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
import math
from collections import deque, defaultdict
import heapq
INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)
        pass

    def add_edge(self, from_, to_, weight=1):
        self.E[from_].append((to_, weight))
        self.E[to_].append((from_, weight))


INF = float("inf")


def solve(N: int, u: int, v: int, A: "List[int]", B: "List[int]"):
    g = Graph(N)
    for a, b in zip(A, B):
        g.add_edge(a-1, b-1)

    ddhouse = [0]*N

    def dfs(f_, pre, dep):
        ddhouse[f_] = dep

        for t_, w in g.E[f_]:
            if t_ == pre:
                continue
            dfs(t_, f_, dep+1)
        return

    dfs(v-1, -1, 0)

    ffhouse = [0]*N

    def dfs(f_, pre, dep):
        ffhouse[f_] = dep

        for t_, w in g.E[f_]:
            if t_ == pre:
                continue
            dfs(t_, f_, dep+1)
        return

    dfs(u-1, -1, 0)
    m = 0
    for d, f in zip(ddhouse, ffhouse):
        if f >= d:
            continue
        else:
            m = max(d, m)
    print(max(m-1, 0))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = int(next(tokens))  # type: int
    v = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, u, v, A, B)


if __name__ == '__main__':
    main()

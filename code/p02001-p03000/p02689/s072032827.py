#!/usr/bin/env python3
import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, src, dest, w=1):
        self.E[src].append((dest, w))
        self.E[dest].append((src, w))  # 無向グラフ


def solve(N: int, M: int, H: "List[int]", A: "List[int]", B: "List[int]"):
    g = Graph(N)

    for a, b in zip(A, B):
        g.add_edge(a-1, b-1)

    cnt = 0
    for node in range(N):
        if all([H[child] < H[node] for child, w in g.E[node]]):
            cnt += 1
    print(cnt)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, H, A, B)


if __name__ == '__main__':
    main()

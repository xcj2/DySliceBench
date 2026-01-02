#!/usr/bin/env python3
from collections import deque
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):
    G = [[] for _ in range(N)]
    for ui, vi, wi in zip(u, v, w):
        ui -= 1
        vi -= 1
        G[ui].append((vi, wi))
        G[vi].append((ui, wi))
    color = [-1] * N
    color[0] = 0
    q = deque([0])
    while q:
        s = q.popleft()
        for t, wi in G[s]:
            if color[t] >= 0:
                continue
            color[t] = (color[s] + wi) % 2
            q.append(t)
    for colori in color:
        print(colori)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    w = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)


if __name__ == '__main__':
    main()

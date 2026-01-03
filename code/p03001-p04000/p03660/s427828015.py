#!/usr/bin/env python3
from collections import deque
import sys
try:
    from typing import Deque, List
except ImportError:
    pass


def bfs(G: "List[List[int]]", a: int):
    q = deque()  # type: Deque[int]
    q.append(a)
    dist = [-1] * len(G)
    dist[a] = 0
    while q:
        s = q.popleft()
        for t in G[s]:
            if dist[t] >= 0:
                continue
            q.append(t)
            dist[t] = dist[s] + 1
    return dist


def solve(N: int, a: "List[int]", b: "List[int]"):
    G = [[] for i in range(N)]
    for ai, bi in zip(a, b):
        ai -= 1
        bi -= 1
        G[ai].append(bi)
        G[bi].append(ai)
    db = bfs(G, 0)
    dw = bfs(G, N - 1)
    bn = sum((dbi <= dwi) for dbi, dwi in zip(db, dw))
    wn = N - bn
    if bn > wn:
        print("Fennec")
    else:
        print("Snuke")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


if __name__ == '__main__':
    main()

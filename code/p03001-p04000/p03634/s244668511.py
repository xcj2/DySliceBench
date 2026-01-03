#!/usr/bin/env python3
from collections import deque
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", Q: int,
          K: int, x: "List[int]", y: "List[int]"):
    G = [[] for _ in range(N)]
    for ai, bi, ci in zip(a, b, c):
        ai -= 1
        bi -= 1
        G[ai].append((bi, ci))
        G[bi].append((ai, ci))

    m = [-1] * N
    q = deque()
    K -= 1
    m[K] = 0
    q.append(K)
    while q:
        i = q.popleft()
        for j, cj in G[i]:
            if m[j] >= 0:
                continue
            m[j] = m[i] + cj
            q.append(j)

    for xi, yi in zip(x, y):
        xi -= 1
        yi -= 1
        print(m[xi] + m[yi])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    c = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, a, b, c, Q, K, x, y)


if __name__ == '__main__':
    main()

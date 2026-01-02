#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, Q: int, L: "List[int]", R: "List[int]", p: "List[int]", q: "List[int]"):
    t = [[0] * (N + 1) for _ in range(N + 1)]
    for Li, Ri in zip(L, R):
        Li -= 1
        Ri -= 1
        t[Li + 1][Ri + 1] += 1
    for i in range(N):
        for j in range(N + 1):
            t[i + 1][j] += t[i][j]
    for i in range(N + 1):
        for j in range(N):
            t[i][j + 1] += t[i][j]
    for pi, qi in zip(p, q):
        pi -= 1
        qi -= 1
        print(t[N][qi + 1] - t[pi][qi + 1])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]"
    q = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    solve(N, M, Q, L, R, p, q)


if __name__ == '__main__':
    main()

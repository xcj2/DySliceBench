#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, C: "List[int]", S: "List[int]", F: "List[int]"):
    def f(i: int, s: int):
        if i == N - 1:
            return s
        s = max(s, S[i])
        return f(i + 1, -(-s // F[i]) * F[i] + C[i])
    for i in range(N):
        print(f(i, 0))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int()] * (N - 1)  # type: "List[int]"
    S = [int()] * (N - 1)  # type: "List[int]"
    F = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        C[i] = int(next(tokens))
        S[i] = int(next(tokens))
        F[i] = int(next(tokens))
    solve(N, C, S, F)


if __name__ == '__main__':
    main()

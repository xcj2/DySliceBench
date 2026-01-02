#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: "List[int]"):
    r = 0
    r += abs(A[0])
    for i in range(N - 1):
        r += abs(A[i] - A[i + 1])
    r += abs(A[-1])
    for i in range(N):
        pp = (0 if i == 0 else A[i - 1])
        np = (0 if i == N - 1 else A[i + 1])
        print(r - abs(A[i] - pp) - abs(A[i] - np) + abs(pp - np))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()

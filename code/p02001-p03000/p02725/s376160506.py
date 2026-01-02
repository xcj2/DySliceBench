#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(K: int, N: int, A: "List[int]"):
    print(K - max((A[i] - A[i - 1]) % K for i in range(N)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(K, N, A)


if __name__ == '__main__':
    main()

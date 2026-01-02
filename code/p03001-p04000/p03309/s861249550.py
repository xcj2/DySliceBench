#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: "List[int]"):
    s = sorted(Ai - i - 1 for i, Ai in enumerate(A))
    b = s[N // 2]
    print(sum(abs(Ai - i - 1 - b) for i, Ai in enumerate(A)))


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

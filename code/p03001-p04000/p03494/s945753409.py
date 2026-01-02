#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

MOD = 2  # type: int


def solve(N: int, A: "List[int]"):

    def f(ai: int):
        ans = 0
        while ai & 1 == 0:
            ai //= 2
            ans += 1
        return ans

    print(min(f(ai) for ai in A))


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

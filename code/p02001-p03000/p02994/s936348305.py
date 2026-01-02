#!/usr/bin/env python3
import sys


def solve(N: int, L: int):

    taste = []
    taste_abs = []

    for i in range(1, N + 1):
        taste.append(L + i - 1)
        taste_abs.append(abs(L + i - 1))

    idx_delete = taste_abs.index(min(taste_abs))
    taste.pop(idx_delete)
    result = sum(taste)

    print(result)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, L)


if __name__ == "__main__":
    main()

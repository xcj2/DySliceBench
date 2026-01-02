#!/usr/bin/env python3
import sys


def cnt(n: int):
    i = 1
    ans = 0
    while i * i < n:
        if n % i == 0:
            ans += 1
        i += 1
    ans *= 2
    if i * i == n:
        ans += 1
    return ans


def solve(N: int):
    print(sum(1 for i in range(1, N + 1, 2) if cnt(i) == 8))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()

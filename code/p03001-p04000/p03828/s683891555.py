#!/usr/bin/env python3
from collections import Counter
from functools import reduce
import sys


def fc(n: int):
    for p in range(2, n + 1):
        while 1:
            q, r = divmod(n, p)
            if r != 0:
                break
            yield p
            n = q
        if n == 1:
            break


MOD = 1000000007  # type: int


def solve(N: int):
    fs = Counter()
    for i in range(1, N + 1):
        fs.update(fc(i))
    print(reduce(lambda a, b: a * (b + 1) % MOD, fs.values(), 1))


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

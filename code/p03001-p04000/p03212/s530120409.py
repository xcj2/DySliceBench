#!/usr/bin/env python3
from itertools import product
import sys


def solve(N: int):
    sN = str(N)
    ans = 0
    for i in range(1, len(sN) + 1):
        for p in product("357", repeat=i):
            if len(set(p)) == 3 and int("".join(p)) <= N:
                ans += 1
    print(ans)


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

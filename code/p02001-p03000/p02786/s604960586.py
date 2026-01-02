#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(H: int):
    from math import ceil
    from functools import lru_cache

    @lru_cache(None)
    def f(n: int):
        if 0 < n <= 1:
            return 1
        
        return 1 + f((n//2)) + f((n//2))

    print(f(H))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    solve(H)

if __name__ == '__main__':
    main()

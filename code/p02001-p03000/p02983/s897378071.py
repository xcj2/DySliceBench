#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 2019  # type: int

def solve(L: int, R: int):
    mn = 2018
    for i in range(L, min(L + 2019, R + 1)):
        mn = min(mn, i % MOD)
    if mn == 0:
        ret = 0
    else:
        ret = float('inf')
        for i in range(L, R):
            for j in range(i + 1, R + 1):
                ret = min(ret, (i * j) % MOD)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(L, R)

if __name__ == '__main__':
    main()

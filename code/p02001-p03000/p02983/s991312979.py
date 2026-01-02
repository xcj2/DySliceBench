#!/usr/bin/env python3
import sys

MOD = 2019  # type: int

def solve(L: int, R: int):
    m = L // MOD
    r = L % MOD
    L -= MOD * (m + 1) # -2019 <= L <= -1
    R -= MOD * (m + 1)
    minmod = sys.maxsize
    upperbound = min(L + MOD, R + 1)
    for i in range(L, upperbound):
        for j in range(i + 1, upperbound):
            minmod = min(minmod, (i * j) % MOD)
    for i in range(L, upperbound):
        if i + MOD <= R:
            minmod = min(minmod, (i * i) % MOD)
    print(minmod)
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

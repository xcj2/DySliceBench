#!/usr/bin/env python3
import sys
# sys.setrecursionlimit(10000000)
INF = 1<<32
# import numpy as np

MOD = 1000000007  # type: int

def solve(n: int, a: int, b: int):
    def combination_with_mod(n, r, mod=10**9+7):
        n1, r = n+1, min(r, n-r)
        numer = denom = 1
        for i in range(1, r+1):
            numer = numer * (n1-i) % mod
            denom = denom * i % mod
        return numer * pow(denom, mod-2, mod) % mod

    ans = pow(2, n, MOD)-combination_with_mod(n, a)-combination_with_mod(n, b)-combination_with_mod(n, 0)

    if ans < 0:
        print((MOD+ans)%MOD)
    else:
        print(ans%MOD)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(n, a, b)

if __name__ == '__main__':
    main()

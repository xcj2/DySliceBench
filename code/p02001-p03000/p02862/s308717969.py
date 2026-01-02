#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(X: int, Y: int):
    def combination(n, r, mod=10**9+7):
        n1, r = n+1, min(r, n-r)
        numer = denom = 1
        for i in range(1, r+1):
            numer = numer * (n1-i) % mod
            denom = denom * i % mod
        return numer * pow(denom, mod-2, mod) % mod

    if (X+Y)%3 != 0 or not (X <= 2*Y and Y <= 2*X):
        print(0)
        exit()

    n = (X+Y)//3
    r = Y-n

    print(combination(n, r))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)

if __name__ == '__main__':
    main()

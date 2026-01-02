#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


class Combination(object):

    def __init__(self, N, mod):
        fac, finv, inv = [0]*(N+1), [0]*(N+1), [0]*(N+1)
        fac[:2] = 1, 1
        finv[:2] = 1, 1
        inv[1] = 1
        for i in range(2, N+1):
            fac[i] = fac[i-1]*i % mod
            inv[i] = -inv[mod % i]*(mod//i) % mod
            finv[i] = finv[i-1]*inv[i] % mod
        self.N = N
        self.MOD = mod
        self.fac = fac
        self.finv = finv
        self.inv = inv

    def __call__(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] * (self.finv[k]*self.finv[n-k] % self.MOD) % self.MOD


def div(a, b):
    return (a * pow(b, MOD-2, MOD)) % MOD


def solve(n: int, k: int):

    cmb = Combination(2*n, MOD)
    if n - 1 <= k:
        print(cmb(2*n-1, n))
        return
    else:
        b = 0
        for i in range(k+1):
            b += cmb(n-1, i)*cmb(n, i)
            b %= MOD
        print(b % MOD)
        return
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(n, k)


if __name__ == '__main__':
    main()

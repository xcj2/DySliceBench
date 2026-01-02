#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")

MOD = 1000000007  # type: int


class Combination(object):

    def __init__(self, N, mod=MOD):
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
        fac = self.fac
        finv = self.finv
        mod = self.MOD
        return fac[n] * (finv[k]*finv[n-k] % mod) % mod


def main():
    K = int(input())
    S = input()

    A = len(S)-1
    cmb = Combination(K+A)
    ans = 0
    for k in range(K+1):
        b = 1
        b *= pow(26, k, MOD)
        b %= MOD
        b *= pow(25, K-k, MOD)
        b %= MOD
        b *= cmb(K-k+A, A)
        # print(cmb(K-k+A, A))
        b %= MOD
        ans += b
        ans %= MOD
    print(ans)
    return


if __name__ == '__main__':
    main()

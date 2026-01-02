#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


class Combination(object):

    def __init__(self, N, mod=10**9+7):
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


def solve(r: "List[int]", c: "List[int]"):

    cmb = Combination(r[1]+c[1]+1, mod=MOD)

    def f(x, y):
        return cmb(x+y, y)

    def g(x, y):
        return f(x+1, y)+f(x, y+1)-1

    ans = g(r[1], c[1])-g(r[0]-1, c[1])-g(r[1], c[0]-1)+g(r[0]-1, c[0]-1)
    print(ans % MOD)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = [int()] * (2)  # type: "List[int]"
    c = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(r, c)


if __name__ == '__main__':
    main()

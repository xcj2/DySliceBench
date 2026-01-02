#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


class Combination(object):
    """
    組み合わせを求める。
    cmbで使いうる最大のNまでを前処理で準備。
    """

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


def solve(X: int, Y: int):

    if X > Y:
        X, Y = Y, X
    sub = Y-X

    if (X - (Y-X)) % 3 != 0:
        print(0)
        return

    A = (X - (Y-X))//3 + sub
    B = (X - (Y-X))//3

    cmb = Combination(A+B)
    print(cmb(A+B, A))

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

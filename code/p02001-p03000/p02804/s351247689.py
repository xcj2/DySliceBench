#!/usr/bin/env python3
import sys
import functools
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


def solve(N: int, K: int, A: "List[int]"):

    cmb = Combination(N, mod=MOD)

    A.sort()

    ans = 0
    for i in range(N):
        # A[i]が最大として選ばれるケース
        if i >= K-1:
            ans += cmb(i, K-1)*A[i]
            ans %= MOD

        # A[i]が最小として選ばれるケース
        if N-i-1 >= K-1:
            ans -= cmb(N-i-1, K-1)*A[i]
            ans %= MOD
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == '__main__':
    main()

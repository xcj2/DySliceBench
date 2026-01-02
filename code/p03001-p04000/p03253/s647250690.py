#!/usr/bin/env python
# coding: utf-8

import math
from operator import mul
from functools import reduce


inf = 10**9+7


# nCr
def combination(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


# nまでの素数を列挙する
class PrimeUtil:
    def __init__(self, n):
        self.l_is_prime = [True for _ in range(n+1)]
        self.l_is_prime[0] = False
        self.l_is_prime[1] = False
        self.n = n
        self.primes = []
        for k in range(2, n+1):
            if self.l_is_prime[k]:
                self.primes.append(k)
                self._set_false(k)

    # pの倍数全てのl_is_primeのフラグをFalseにする
    def _set_false(self, p):
        k = p
        for _ in range(1, self.n//p):
            k += p
            self.l_is_prime[k] = False

    # 素因数分解した結果を返す
    def factor(self, k):
        ret = {}
        tmp = k
        for p in self.primes:
            if p > tmp:
                break
            while True:
                if tmp % p != 0:
                    break
                ret.setdefault(p, 0)
                ret[p] += 1
                tmp /= p
                if tmp == 1:
                    break
        if tmp > 1:
            ret[tmp] = 1
        return ret


def main():
    N, M = list(map(int, input().split()))
    pu = PrimeUtil(100000)
    ans = 1
    f = pu.factor(M)
    for v in f.values():
        ans *= combination(v+N-1, v)
        ans %= inf
    print(ans)


if __name__ == '__main__':
    main()

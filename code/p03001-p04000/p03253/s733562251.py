# -*- coding: utf-8 -*-
import unittest
import math

MOD = 10**9+7


def func(n,m):
    fac = [1 for _ in range(n+100)]
    finv = [1 for _ in range(n+100)]
    inv = [1 for _ in range(n+100)]
    for i in range(2,n+100):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = (MOD - inv[MOD%i] * (MOD//i))%MOD
        finv[i] = (finv[i-1]*inv[i])%MOD

    def comb(a,b):
        return (fac[a]*((finv[b]*finv[a-b])%MOD))%MOD

    fact = {}
    for x in range(2, math.ceil(math.sqrt(m))+1):
        while m%x==0:
            if x not in fact:
                fact[x] = 0
            fact[x] += 1
            m = m//x
        if m==1:
            break
    if m!=1:
        fact[m] = 1

    ret = 1
    for k in fact.values():
        ret *= comb(k+n-1,k)
        ret %= MOD
    return ret

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func(2,6), 4)
        self.assertEqual(func(3,12), 18)
        self.assertEqual(func(100000, 1000000000), 957870001)
        self.assertEqual(func(2,3), 2)

if __name__ == '__main__':
    n,m = map(int, input().split())
    print(func(n,m))
    # unittest.main()

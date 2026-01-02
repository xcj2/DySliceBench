# -*- coding: utf-8 -*-
def primeFactors(n):
    res = []
    while n%2==0:
        res.append(2)
        n //= 2
    x = 3
    while n>1 and n>=x*x:
        while n%x==0:
            res.append(x)
            n //= x
        x += 2
    if n>1:
        res.append(n)
    return res

class BiCoeff(object):
    def __init__(self, MAX, m):
        super(BiCoeff, self).__init__()
        fac = [0]*MAX
        finv = [0]*MAX
        inv = [0]*MAX

        fac[0] = 1
        fac[1] = 1
        finv[0] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2,MAX):
            fac[i] = (fac[i-1]*i)%m
            inv[i] = m - (inv[m%i] * (m//i))%m
            finv[i] = (finv[i-1] * inv[i])%m

        self.MAX = MAX
        self.m = m
        self.fac = fac
        self.finv = finv
        self.inv = inv

    def calc(self,n,k):
        if n<k:
            return 0
        if n<0 or k<0:
            return 0
        return (self.fac[n] * (self.finv[k]*self.finv[n-k])%self.m)%self.m

from collections import defaultdict
MOD = 10**9 + 7
n,m = map(int, input().split())

bicoeff = BiCoeff(n+100,MOD)

d = defaultdict(int)
for p in primeFactors(m):
    d[p] += 1

res = 1
for v in d.values():
    res *= bicoeff.calc(n-1+v,n-1)
    res %= MOD
print(res)

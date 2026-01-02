#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

class InverseTable:
    __slots__ = ['In', 'fac', 'Ifac']

    def __init__(self, mod, maxnum):
        self.In = [0, 1]; self.fac = [1, 1]; self.Ifac = [1, 1]
        for i in range( 2, maxnum + 1 ):
            self.In.append( ( -self.In[mod % i] * (mod//i) ) % mod )
            self.fac.append( ( self.fac[-1] * i ) % mod )
            self.Ifac.append( (self.Ifac[-1] * self.In[-1]) % mod )
        
    def cmb(self, n, r):
        if ( r<0 or r>n ): return 0
        r = min(r, n-r)
        over = 1
        for i in range(n,n-r,-1):
          over *= i; over %= mod
        
        return over * self.Ifac[r]  % mod
        # return self.fac[n] * self.Ifac[r] * self.Ifac[n-r] % mod
    
    def per(self, n, r):
        if ( r<0 or r>n ): return 0
        return self.fac[n] * self.Ifac[n-r] % mod

invt = InverseTable(mod, 10**6)
# maxnum=10**6だとテーブル生成に200ms程かかるので（Pythonだと1000msほど）
# 最大生成領域は問題ごとに要検討

from operator import mul
from functools import reduce

def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

def ncr(n, r):
    r = min(r, n - r)
    if r == 0: return 1;
    if r == 1: return n;
    numerator = [n - r + i + 1 for i in range(r)]
    denominator  = [i + 1 for i in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1: 
            result *= numerator[k]
            result %= mod
    return result

# N = 10000
# cnt = 0
# for a in xrange(N + 1):
#     cnt += ncr(N, a)

# print cnt == 2 ** N

n,a,b=map(int,input().split())
ans += pow(2,n,mod)-1
ans -= invt.cmb(n,a)
ans -= invt.cmb(n,b)
print(ans%mod)
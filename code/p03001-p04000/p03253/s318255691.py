#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,m = map(int,input().split())
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
        return self.fac[n] * self.Ifac[r] * self.Ifac[n-r] % mod
    
    def per(self, n, r):
        if ( r<0 or r>n ): return 0
        return self.fac[n] * self.Ifac[n-r] % mod

invt = InverseTable(mod, 10**6)
# maxnum=10**6だとテーブル生成に200ms程かかるので（Pythonだと1000msほど）
# 最大生成領域は問題ごとに要検討

def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        count=0
        while n % i==0:
            count+=1
            n = n//i
        if count!=0:
            ass.append((i,count))
    if n != 1:
        ass.append((n,1))
    return ass


ass = prime_factor(m)
ans = 1
for i, amount in ass:
  ans = ans * invt.cmb(amount+n-1,amount) % mod
print(ans)
# print(ass)

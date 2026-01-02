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
            self.fac.append( ( self.fac[-1] * i ) % mod )
            self.In.append( ( -self.In[mod % i] * (mod//i) ) % mod )
            self.Ifac.append( (self.Ifac[-1] * self.In[-1]) % mod )
        
    def cmb(self, n, r):
        if ( r<0 or r>n ): return 0
        r = min(r, n-r)
        return self.fac[n] * self.Ifac[r] * self.Ifac[n-r] % mod

invt = InverseTable(mod, 10**6)

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

n=int(input())
A=list(map(int,input().split()))
data=[0]*(10**6+10)
for ai in A:
    arr=prime_factor(ai)
    for ni,ci in arr:
        data[ni]=max(data[ni],ci)
pro=1
for i in range(1,len(data)):
    pro=pro*(i**data[i])
    pro%=mod

for ai in A:
    ans+=invt.In[ai]
print(ans*pro%mod)
#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
A=list(map(int,input().split()))


def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a
    
def lcm(m,n):
    return (m*n)//gcd(m,n)

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

it = InverseTable(mod, 10**6)

for ai in A:
    pro=lcm(pro,ai)
for ai in A:
    ans+=it.In[ai]
    ans%=mod
print((pro*ans)%mod)

# pro2=1
# for ai in A:
#     pro2=(pro2*ai)%mod
#     pro=gcd(pro,ai)
# for ai in A:
#     count+=pro//ai
#     count%=mod
# print(count)
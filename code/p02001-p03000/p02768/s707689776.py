import time
from math import factorial

def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=1
    for i in range(n, n-k, -1):
        a=a * i % mod
    b=framod(k, mod)
    return (a * power(b, mod-2, mod)) % mod

n,a,b=map(int, input().split())
mo=10**9+7

fn=2*10**5
fac=[0]*fn
fac[1]=n

print((power(2, n, mo)-1-comb(n,a,mo)-comb(n,b,mo))%mo)



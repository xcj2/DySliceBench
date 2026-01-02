
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
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

x,y=map(int, input().split())

if y < x:
    tmp=y
    y=x
    x=tmp

if (y-x) > x or (x-(y-x))%3 !=0:
    print(0)
    exit()

mo12=0
mo21=0

if y != x:
    tmp=y-x
    y-=2*tmp
    x-=tmp
    mo12=tmp

mo12+=y/3
mo21+=y/3

print(comb(int(mo12+mo21), int(mo21), 1000000007))

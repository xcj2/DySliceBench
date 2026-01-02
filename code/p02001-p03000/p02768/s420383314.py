import sys
from io import StringIO
import unittest
import math

mod = 10**9+7

def pow_mod(a, b, mod):
    x = 1
    while b > 0:
        if b & 1:
            x = (x*a)%mod
        a = (a**2)%mod
        b //= 2
 
    return x

def modinv(a, mod):
    return pow_mod(a, mod-2, mod)

def comb(n,r,mod):
    combsum=1
    for i in range(n-r+1,n+1):
        combsum = (combsum * i)%mod

    for i in range(1,r+1):
        combsum = (combsum * inv[i])%mod

    return combsum

n,a,b = list(map(int,input().strip().split()))

a=min([a,n-a])
b=min([b,n-b])

maxab=max([a,b])

inv=[modinv(i,mod) for i in range(0,maxab+2)]

def resolve():

    ptn = pow_mod(2,n,mod)
    ptn -= 1

    comba=comb(n,a,mod)
    combb=comb(n,b,mod)

    ptn = (ptn-comba-combb)%mod

    print(ptn)

    return 

resolve()
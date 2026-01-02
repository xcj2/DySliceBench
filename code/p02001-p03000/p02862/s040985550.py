# -*- coding: utf-8 -*-
import math

def mod_factorial(n):
    mod = 10**9+7

    if n < 1:
        return 1

    r = n
    for i in range(n-1):
        r = r*(i+1) % mod
    
    return r

def mod_pow(n,m):

    mod = 10**9+7
    r = 1

    while m > 0:
        if m & 1:
            r = r*n % mod
        n = n * n % mod
        m = m>>1

    return(r)



def mod_comb(n, k):
    mod = 10**9+7

    if n+k < 1:
        return 1
    
    a = mod_factorial(n)
    b = mod_pow(mod_factorial(k), mod-2)
    c = mod_pow(mod_factorial(n-k), mod-2)


    return (a * ((b * c) % mod)) % mod


a, b= map(int, input().split())

t = [a,b]

r = 0
mod = 10**9+7

x = (2*a-b)
y = (2*b-a)

if x%3 == 0 and y%3 == 0 and x*y >=0:
    m = int(x/3)
    n = int(y/3)

    r += mod_comb(n+m,m)

print(r)
import numpy as np
import math
from math import factorial

# K = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# S = input() # String

mod = 1000000000 + 7

fact_table = dict()

def dupcomb(n, k, p):
    return comb(n+k-1, k, p)

def comb(n,k,p):
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1

    if n in fact_table:
        a = fact_table[n]
    else:
        a=factorial(n) %p
        fact_table[n] = a

    if k in fact_table:
        b = fact_table[k]
    else:
        b=factorial(k) %p
        fact_table[k] = b
        
    if n-k in fact_table:
        c = fact_table[n-k]
    else:
        c=factorial(n-k) %p
        fact_table[n-k] = c
        
    return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p

def power_func(a,b,p):
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p


def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

N, M = map(int, input().split())

primes = factorize(M)

count = 1

fk_save = dict()

for pair in primes:
    k = pair[1]
    # print('k=', k)

    if k in fk_save:
        fk = fk_save[k]
    else:
        fk = dupcomb(N, k, mod)
        fk_save[k] = fk
    # print('fk=', fk)

    count = (fk * count) % mod
    # print('count=', count)
    
print(count)
# ret = comb(10, 5, mod)
# print(ret)

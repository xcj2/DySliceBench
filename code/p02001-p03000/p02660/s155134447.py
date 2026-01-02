import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

import math # version 3.5 >
from collections import defaultdict
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def lcm(*numbers):
    return reduce(lambda x,y: (x * y) // math.gcd(x, y), numbers, 1)

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

n=n_in()
f=factorize(n)



res = 0

for _,i in f:
    j=1
    while i-j >= 0:
        i=i-j
        j+=1
        res += 1

print(res)

import numpy as np
from operator import mul
from functools import reduce
def modmul(a,b):
    return a * b % 1000000007
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
def modinv(a, m):
    g, x, y = xgcd(a, m)
    return x % m
def comb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(modmul, range(n, n - r, -1))
    under = reduce(modmul, range(1,r + 1))
    return over * modinv(under, 1000000007)
def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K = (K * x) % 1000000007
        x = (x * x) % 1000000007
        n //= 2
    return (K * x) % 1000000007
n,a,b = (int(x) for x in input().split())
binary = bin(n)
l = []
for i in range(1,len(binary)-1):
    if binary[-i] == "1":
        l.append(pow_k(2,pow_k(2,i-1)))
prod = 1
for value in l:
    prod = (prod * value) % 1000000007
print((prod-(1+(comb(n, a)%1000000007)+(comb(n, b)%1000000007)))%1000000007)
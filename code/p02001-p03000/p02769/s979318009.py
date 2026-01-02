import sys
from math import factorial
n, k = [int(i) for i in sys.stdin.readline().split()]
mod = 10**9+7
fact_ls = [1]
res = 1
for i in range(1, n+1):
    res = res * i % mod
    fact_ls.append(res)

def my_fact(r):
    return fact_ls[r]

def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2] // w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    # [x,y]
    return [w[0], w[1]]


# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m + x % m) % m

def nCr(n, r, mod):
    a = my_fact(r)
    b = 1
    for i in range(1, r + 1):
        b = b * (n - i + 1) % mod
    a = mod_inv(a, mod)
    return b * a

def nHr(n, r, mod):
    return nCr(n + r - 1, r, mod)

def calc_func(n, r):
    a = my_fact(r)
    c = my_fact(n - r)
    b = my_fact(n)
    d = my_fact(n-1)
    e = my_fact(n-1-r)
    a = mod_inv(a, mod)
    c = mod_inv(c, mod)
    e = mod_inv(e, mod)
    return b * a * c % mod * d * e * a % mod

res = 1
for i in range(1, min(n, k + 1)):
    res = (res + calc_func(n, i)) % mod
print(res)
import sys
from math import factorial


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
    a = factorial(r)
    b = 1
    for i in range(1, r + 1):
        b = b * (n - i + 1) % mod
    a = mod_inv(a, mod)
    return b * a

n, a, b = [int(i) for i in sys.stdin.readline().split()]
mod = 10 ** 9 + 7
res = 2 ** n % mod
res -= (nCr(n, a, mod) + nCr(n, b, mod) + 1) % mod
if res < 0:
    res += mod
print(res)
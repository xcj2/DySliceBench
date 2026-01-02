import numpy as np
MOD = 10**9 + 7
def extgcd(a, b):
    r = np.array([1,0,a], dtype=int)
    w = np.array([0,1,b], dtype=int)
    while w[2] != 1:
        q = r[2] // w[2]
        r, w = w, r - q*w
    return w[:2]

def mod_inverse(a, m):
    x, y = extgcd(a, m)
    return (m + x % m) % m

def solve(x, y):
    a = -y + 2*x
    b = 2*y - x
    if (a < 0) or (b < 0):
        return 0
    if a % 3 + b % 3 != 0:
        return 0
    a //= 3
    b //= 3
    n, k = a+b, a
    p, q = 1, 1
    for i in range(k):
        p = p * (n-i) % MOD
        q = q * (i+1) % MOD
    return (p * mod_inverse(q, MOD)) % MOD

x, y = map(int, input().split())
print(solve(x, y))
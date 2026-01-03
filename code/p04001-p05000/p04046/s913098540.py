import operator as op
from functools import reduce

MOD = (10 ** 9) + 7

factors = [1, 1]
finv = [1, 1]
inv = [0, 1]

for i in range(2, 200010):
    factors.append(factors[i - 1] * i % MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[i - 1] * inv[i] % MOD)

def nck(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return factors[n] * (finv[k]  * finv[n - k] % MOD) % MOD

def ncr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

assert ncr(3, 4) == 0

def g(h, w, a, b):
    prev = [1] * w
    cur = [0] * w

    for i in range(h - 1):
        cur[0] = 1
        start = 0
        if i >= h - 1 - a:
            cur[b] = prev[b]
            start = b
        for j in range(start + 1, w):
            cur[j] = cur[j - 1] + prev[j]
            cur[j] = cur[j] % (1e9 + 7)
        prev, cur = cur, prev
    return prev[-1]

def f(H, W, A, B):
    count = 0
    x, y, a = H - A - 1, W + A - 2, A - 1
    for i in range(B, W): # bottom-left to top-right
        c1 = nck(x + i, i)
        c2 = nck(y - i, a)
        c = c1 * c2
        count += c
        count = count % MOD
    return int(count)

## assert f(4, 4, 0, 0) == 20
# assert f(4, 4, 2, 2) == 10
#assert f(2, 3, 1, 1) == 2
#assert f(10, 7, 3, 4) == 3570
#assert f(100000, 100000, 99999, 99999) == 1
#assert f(100000, 100000, 44444, 55555) == 738162020

H, W, A, B = map(int, input().split())
ans = f(H, W, A, B)
print(ans)

from math import sqrt
from collections import defaultdict

n, m = [int(i) for i in input().split()]

A = defaultdict(int)
p = 10 ** 9 + 7

def fact(n, p=10**9 + 7):
    f = [1]
    for i in range(1, n+1):
        f.append(f[-1]*i%p)
    return f

def invfact(n, f, p=10**9 + 7):
    inv = [pow(f[n], p-2, p)]
    for i in range(n, 0, -1):
        inv.append(inv[-1]*i%p)
    return inv[::-1]

f = fact(30+10**5)
invf = invfact(30+10**5, f)

def comb(a, b):
    return f[a] * invf[b] * invf[a-b] % p

i = 2

while m != 1 and i <= sqrt(m) + 1:
    while m % i == 0:
        m //= i
        A[i] += 1
    i += 1

if m != 1:
    A[m] = 1

n -= 1
ans = 1

for v in A.values():
    ans *= comb(v+n, n)
    ans %= p

print(ans)
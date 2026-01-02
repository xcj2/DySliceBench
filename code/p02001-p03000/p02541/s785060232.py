import sys
from itertools import product
def I(): return int(sys.stdin.readline().rstrip())


def ext_gcd(a, b):
    if b:
        d, y, x = ext_gcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


# V = [(X_i, Y_i), ...]: X_i (mod Y_i)
def remainder(V):
    x = 0; d = 1
    for X, Y in V:
        g, a, b = ext_gcd(d, Y)
        x, d = (Y*b*x + d*a*X) // g, d*(Y // g)
        x %= d
    return x, d


def prime_factorization(n):
    res = {}
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            r = 0  # nがiで何回割り切れるか
            while n % i == 0:
                n //= i
                r += 1
            res[i] = r
    if n != 1:
        res[n] = 1
    return res


N = I()

prime_fac = prime_factorization(N)
if 2 in list(prime_fac.keys()):
    prime_fac[2] += 1
else:
    prime_fac[2] = 1

# prime_fac = 2*N の素因数分解
# 2*N|k*(k+1)
# 中国剰余定理を用いる

A = list(prime_fac.keys())
l = len(A)

ans = 2*N

for a in list(product([-1,0],repeat=l)):
    V = [(a[i],A[i]**prime_fac[A[i]]) for i in range(l)]
    x,d = remainder(V)
    if x != 0:
        ans = min(ans,x)

print(ans)

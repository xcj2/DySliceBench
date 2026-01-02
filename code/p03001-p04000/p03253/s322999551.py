from math import sqrt, ceil, factorial
from collections import Counter

m = 10**9+7
def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, ceil(sqrt(n))+1):
        if n % i == 0: return False
    return True

def prime_factorization(n):
    if is_prime(n):return [n]
    factor = []
    f = 2
    while n > 1:
        if n % f == 0:
            factor.append(f)
            n /= f
        else:
            f += 1
    return factor

def comb(n, r):
    a = 1
    for i in range(n-r+1, n+1):
        a *= i
    return a//factorial(r)

N, M = map(int, input().split())
p = prime_factorization(M)
c = Counter(p)
ans = 1
for v in c.values():
    ans *= (comb(v + N - 1, v) % m)
print(ans%m)
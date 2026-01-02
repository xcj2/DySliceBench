from math import gcd, sqrt, ceil
from functools import reduce

def sieve(n):
    A = list(range(n+1))
    for i in range(2, n+1 ,2):
        A[i] = 2
    for j in range(3, ceil(sqrt(n+1))+1, 2)[::-1]:
        for i in range(j, n+1, j):
            A[i] = j
    return A

def factorize(n, A):
    factors = set()
    while n != 1:
        f = A[n]
        factors.add(f)
        n //= f
    return factors

# def factorize(n):
#     factors = set()
#     if n % 2 == 0:
#         factors.add(2)
#         n //= 2
#     while n % 2 == 0:
#         n //= 2
#     for i in range(3, ceil(sqrt(n + 1)) + 1):
#         if n % i == 0:
#             factors.add(i)
#             n //= i
#         while n % i == 0:
#             n //= i
#     if n > 2:
#         factors.add(n)
#     return factors

_, *aa = map(int, open(0).read().split())

def main(aa):
    pair_co = True
    A = sieve(10**6)
    all_factors = set()
    for a in aa:
        factors = factorize(a, A)
        for factor in factors:
            if factor in all_factors:
                pair_co = False
                break
            else:
                all_factors.add(factor)
        if not pair_co:
            break
    if pair_co:
        return 'pairwise coprime'
    elif reduce(gcd, aa) == 1:
        return 'setwise coprime'
    else:
        return 'not coprime'

print(main(aa))
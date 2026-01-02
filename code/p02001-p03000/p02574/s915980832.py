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

_, *aa = map(int, open(0).read().split())

def main(aa):
    pair_co = True
    A = sieve(10**6)
    all_factors = [0] * (10**6+1)
    for a in aa:
        factors = factorize(a, A)
        for factor in factors:
            if all_factors[factor]:
                pair_co = False
                break
            else:
                all_factors[factor] = 1
        if not pair_co:
            break
    if pair_co:
        return 'pairwise coprime'
    elif reduce(gcd, aa) == 1:
        return 'setwise coprime'
    else:
        return 'not coprime'

print(main(aa))
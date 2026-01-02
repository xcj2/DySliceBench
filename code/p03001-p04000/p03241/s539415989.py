import math, operator
from collections import Counter
from itertools import chain, product, permutations, combinations
from functools import reduce, lru_cache
class PrimeUtils:
    @staticmethod
    def primes_sieve(n):
        sieve = [True] * (n + 1)
        for i in range(2, n + 1):
            if sieve[i]:
                for j in range(i + i, n + 1, i):
                    sieve[j] = False
        return [i for i, x in enumerate(sieve[2:], 2) if x]
    @classmethod
    # Prime Factor Decomposition
    def pfd(cls, n):
        rn = math.ceil(math.sqrt(n))
        primes = cls.primes_sieve(rn)

        factors = []
        cur = n
        for p in primes:
            while True:
                div, rem = divmod(cur, p)
                if rem == 0:
                    factors.append(p)
                    cur = div
                else:
                    break
        if cur != 1 or not factors:
            factors.append(cur)
        return factors
    @classmethod
    # List up aliquots
    def aliquots(cls, n):
        pf = cls.pfd(n)
        pfc = Counter(pf)
        ppv = [[pow(p, i) for i in range(n+1)] for p,n in pfc.items()]
        return map(lambda x: reduce(operator.imul, x), product(*ppv))

N, M = map(int, input().split())
for factor in sorted(PrimeUtils.aliquots(M)):
    if N <= factor:
        print(M // factor)
        break
else:
    print(1)
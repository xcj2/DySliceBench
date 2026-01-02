import types, math, operator
import numpy as np
from math import sqrt
from collections import Counter
from itertools import product
from functools import reduce
class PrimeUtils:
    @staticmethod
    def _has_numpy():
        g = globals()
        m = g.get('np')
        if m is not None and isinstance(m, types.ModuleType):
            return  m.__name__ == 'numpy'
        return False
    @staticmethod
    def _primes_sieve_pp(n):
        sieve = [True] * (n + 1)
        for i in range(2, int(sqrt(n)) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i, x in enumerate(sieve[2:], 2) if x]
    @staticmethod
    def _primes_sieve_np(n):
        sieve = np.ones(n + 1, np.bool)
        sieve[0] = sieve[1] = False
        for i, v in enumerate(sieve[2:int(sqrt(n)) + 1], 2):
            if v: sieve[i*i::i] = False
        return np.nonzero(sieve)[0]
    @staticmethod
    def _primes_sieve_np_fast(n):
        n += 1
        sieve = np.ones(n//3 + (n%6 == 2), dtype=np.bool)
        check_upper = int(sqrt(n)) // 3
        for i, v in enumerate(sieve[1:check_upper + 1], 1):
            if v:
                k = (3*i + 1) | 1
                sieve[k* k           //3::2*k] = False
                sieve[k*(k-2*(i&1)+4)//3::2*k] = False
        sieve[0] = False
        return np.r_[2,3,((3*np.nonzero(sieve)[0] + 1)|1)]
    @classmethod
    def primes_sieve(cls, n):
        if cls._has_numpy():
            return cls._primes_sieve_np_fast(n)
        else:
            return cls._primes_sieve_pp(n)
    # Prime Factor Decomposition
    @classmethod
    def pfd(cls, primes, n):
        # primes = cls.primes_sieve(n)

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
        assert(cur == 1)
        return factors
    # List up aliquots
    @classmethod
    def aliquots(cls, n):
        pf = cls.pfd(n)
        pfc = Counter(pf)
        ppv = [[pow(p, i) for i in range(n+1)] for p,n in pfc.items()]
        if not ppv:
            return (1,)
        else:
            return map(lambda x: reduce(operator.imul, x), product(*ppv))

    @classmethod
    def aliquots_n(cls, n):
        pf = cls.pfd(n)
        pfc = Counter(pf)
        ppv = [[pow(p, i) for i in range(n+1)] for p,n in pfc.items()]
        if not ppv:
            return 1
        else:
            return reduce(operator.imul, [len(x) for x in ppv])

import math
fact = math.factorial
N = int(input())

from collections import Counter
primes = PrimeUtils.primes_sieve(N)

cc = Counter()
for n in range(N):
    cc += Counter(PrimeUtils.pfd(primes, n + 1))

cn = Counter()
for n in cc.values():
    if n >= 2:
        cn[3] += 1
    if n >= 4:
        cn[5] += 1
    if n >= 14:
        cn[15] += 1
    if n >= 24:
        cn[25] += 1
    if n >= 74:
        cn[75] += 1
print(sum([
      cn[75],
      cn[15] * (cn[5] - 1) ,
      cn[25] * (cn[3] - 1) ,
      max(0, (cn[3] - cn[5])) * max(0, cn[5]) * max(0, (cn[5] - 1)) // 2,
      cn[5] * max(0, (cn[5] - 1)) * max(0, (cn[5] - 2)) // 2
      ]))
        
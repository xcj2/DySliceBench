N,M = map(int, input().split())
mod = 10 ** 9 + 7

import math
class PrimeUtils:
    @staticmethod
    def primes_sieve(n):
        sieve = [True] * (n + 1)
        for i in range(2, n + 1):
            if sieve[i]:
                for j in range(i + i, n + 1, i):
                    sieve[j] = False
        return [i for i, x in enumerate(sieve[2:], 2) if x]
    @staticmethod
    # Prime Factor Decomposition
    def pfd(n):
        rn = math.ceil(math.sqrt(n))
        primes = PrimeUtils.primes_sieve(rn)

        factors = []
        cur = n
        for p in primes:
            cnt = 0
            while True:
                div, rem = divmod(cur, p)
                if rem == 0:
                    cnt += 1
                    cur = div
                else:
                    break
            if cnt != 0:
                factors.append((p, cnt))
        if cur != 1 or n == 1:
            factors.append((cur, 1))
        return factors

import itertools, operator, math
class Combination:
    def __init__(self, fact=math.factorial, div=operator.itruediv):
        self.fact = fact
        self.div = div
    def C(self, n, m):
        if n < m: return 0
        if m == 0 or n == m: return 1
        return self.div(
                self.fact(n),
                self.fact(n - m) * self.fact(m)
            )
    def H(self, n, r):
        return self.C(n - 1 + r, r)

class GFp:
    def __init__(self, p):
        self.p = p
    def inv(self, v):
        return pow(v, self.p - 2, self.p)

class CachedFactorial:
    def __init__(self, n, mod):
        self.mod = mod
        self.fact_cache = list(
                itertools.accumulate(
                        itertools.chain(
                                [1],
                                range(1, n+1)
                        ),
                        lambda a,x: (a * x) % mod
                )
        )
    def factorial(self, n):
        return self.fact_cache[n]

class CachedComb(Combination):
    def __init__(self, n, mod):
        self.mod = mod
        self.gfp = GFp(mod)

        self.n = n
        self.fact = CachedFactorial(n, mod)
        super().__init__(
             self.fact.factorial,
             lambda x, y: (x * self.gfp.inv(y)) % self.mod
        )

ps = PrimeUtils.pfd(M)
cc = CachedComb(N + max(x[1] for x in ps), mod)
ans = 1
for p, c in ps:
    if p == 1: continue
    cmb = cc.H(N, c)
    ans = ans * cmb % mod
print(ans)
inpl = lambda: list(map(int,input().split()))
from math import sqrt
class Factorizer():
    def __init__(self):
        self.primes_ceil = 3
        self.primes = [2]

    def find_primes(self, primes_ceil):
        prev_primes_ceil, self.primes_ceil = self.primes_ceil, primes_ceil
        for i in range(prev_primes_ceil, self.primes_ceil):
            sieve = 1
            for p in self.primes:
                if p*p > i:
                    break
                elif i % p == 0:
                    sieve = 0
                    break
            if sieve == 0:
                continue
            else:
                self.primes.append(i)

    def __call__(self, n):
        if (self.primes_ceil-1)**2 < n:
            self.find_primes(int(sqrt(n))+1)
        factors = []
        powers = []
        for p in self.primes:
            if p * p > n:
                break
            elif n % p == 0:
                n //= p
                k = 1
                while n % p == 0:
                    n //= p
                    k += 1
                factors.append(p)
                powers.append(k)
        if n > 1:
            factors.append(n)
            powers.append(1)
        return factors, powers

N, P = inpl()
fct=Factorizer()
f, p = fct(P)
n = len(f)
ans = 1
for i in range(n):
    ans *= f[i]**(p[i]//N)
print(ans)
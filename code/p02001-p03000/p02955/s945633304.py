from math import sqrt
class Factorizer:
    def __init__(self):
        self.primes_ceil = 5
        self.primes = [2,3]

    def find_primes(self, primes_ceil):
        if primes_ceil <= self.primes_ceil:
            return self.primes

        prev_primes_ceil, self.primes_ceil = self.primes_ceil, primes_ceil
        r, m = prev_primes_ceil//6, prev_primes_ceil%6
        if m <= 1:
            i = r*6 + 1
            mod_flag = True
        else:
            i = r*6 + 5
            mod_flag = False

        while i < self.primes_ceil:
            sieve = True
            for p in self.primes:
                if p*p > i:
                    break
                elif i % p == 0:
                    sieve = False
                    break
            if sieve:
                self.primes.append(i)
            if mod_flag:
                i += 4
                mod_flag = False
            else:
                i += 2
                mod_flag = True

        return self.primes

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

inpl = lambda: list(map(int,input().split()))
N, K = inpl()
A = inpl()
S = sum(A)
factorize = Factorizer()

ft, pw = factorize(S)
n = len(ft)
denominators = [1]
for i in range(n):
    new_denominators = []
    for d in denominators:
        for p in range(pw[i]+1):
            new_denominators.append(d*(ft[i]**p))
    denominators = new_denominators
denominators.sort(reverse=True)

for d in denominators:
    mods = [a%d for a in A]
    mods.sort()
    Sm = sum(mods)
    h = Sm // d
    minK = min(d*(h+1)-sum(mods[N-h-1:]), sum(mods[:N-h]))
    if minK <= K:
        print(d)
        exit()
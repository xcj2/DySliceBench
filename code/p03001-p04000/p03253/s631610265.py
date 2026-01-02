N, M = list(map(int, input().split()))

MOD = 10**9+7

class Comb:
    def __init__(self, N):
        self.fac = [1] * (N+1)
        for i in range(2, N+1): self.fac[i] = self.fac[i-1] * i % MOD

    def pow(self, a, b):
        res = 1
        while b:
            if b & 1: res = res * a % MOD
            a = a**2 % MOD
            b >>= 1
        return res

    def comb(self, n, r):
        if r < 0 or r > n: return 0
        return (self.fac[n] * self.pow(self.fac[r], MOD-2)) % MOD * self.pow(self.fac[n-r], MOD-2) % MOD

    def permutation(self, n, r):
        if r == 0: return 1
        return self.fac[n] * self.pow(self.fac[n-r], MOD-2) % MOD

from collections import *
import sys
def get_prime(n):
    c = Counter()

    while not n % 2:
        c[2] += 1
        n //= 2
    i = 3

    while i**2 <= n:
        while not n % i:
            c[i] += 1
            n //= i
        i += 2

    if n > 1: 
        c[n] += 1

    return c

prime = get_prime(M)
if not prime: print(1); sys.exit()

comb = Comb(N+max([m for m in prime.values()]))

ans = 1

for n in prime.values():
    ans = ans * comb.comb(N+n-1, n) % MOD
print(ans % MOD)
import sys
from math import gcd
from functools import reduce
input = sys.stdin.buffer.readline

class FLT:
    def __init__(self, mod=10**9+7):
        self.mod = mod

    def rep_sqr(self, base, k):
        ans = 1
        while k > 0:
            if k & 1:
                ans = ans * base % self.mod
            base = base * base % self.mod
            k >>= 1
        return ans

    def inv(self, a):
        """ 逆元を取る """
        return self.rep_sqr(a, self.mod-2)


def gcd_list(numbers):
    return reduce(gcd, numbers)

def euler_phi(n):
    phi = n
    for i in set(prime_factorize(n)):
        phi *= (1 - (1 / i))
    return int(phi)

def prime_factorize(n):
    # Return list of prime factorized result
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n, k = map(int, input().split())
MOD = 10**9 + 7
flt = FLT(MOD)
memo = [-1 for _ in range(k+1)]
ans = 0
for i in range(1, k+1):
    d = k // i
    if memo[d] == -1:
        memo[d] = flt.rep_sqr(d, n)
    ans += memo[d] * euler_phi(i)
print(ans % MOD)
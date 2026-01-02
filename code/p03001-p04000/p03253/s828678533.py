import sys
input = sys.stdin.readline

from collections import *

def prime_fact(n):
    prime = Counter()
    m = 0

    while not n % 2: 
        prime[2] += 1
        n //= 2
        m += 1

    x = 3
    while x**2 <= n: 
        c = 0
        while not n % x: 
            prime[x] += 1
            n //= x
            c += 1
        m = max(m, c)
        x += 2

    if n > 1: prime[n] += 1

    return prime, m

MOD = 10**9+7

class Comb:
    def __init__(self, N):
        self.fac = [1] * (N+5)
        for i in range(2, N+5): self.fac[i] = self.fac[i-1] * i % MOD

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

def main():
    N, M = list(map(int, input().split()))
    prime, m = prime_fact(M)

    comb = Comb(N-1+m)
    ans = 1

    for v in prime.values():
        ans = ans * comb.comb(N-1+v, v) % MOD

    print(ans)
    
if __name__ == '__main__':
    main()
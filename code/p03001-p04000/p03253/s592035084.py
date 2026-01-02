import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
mod = 10**9+7

pos = {}
neg = {}
n = 1
pos[0] = 1
neg[0] = 1
for i in range(1, 500000):
    n *= i
    n %= mod
    pos[i] = n
    neg[i] = pow(n, mod-2, mod)

def prime_factorize(n):
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

from collections import Counter
primes = prime_factorize(M)
c = Counter(primes)
primes = list(set(primes))
leng = len(primes)
ans = 1
for i in range(leng):
    p = primes[i]
    n = c[p]
    ans *= pos[N+n-1]*neg[n]*neg[N-1]
    ans %= mod

print(ans)

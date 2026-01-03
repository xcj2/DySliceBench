import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
mod = 10**9+7
from collections import Counter

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primes.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        primes.append(n)
    return a
primes = []
for i in range(1, N+1):
    prime_factorize(i)
c = Counter(primes)
ans = 1
for n, cnt in c.most_common():
    ans *= (cnt+1)
    ans %= mod
print(ans)
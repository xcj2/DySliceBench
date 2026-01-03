
import collections
import itertools
import sys
import time

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

def get_primes(max_val):
    is_prime = [True] * (max_val + 1)
    for i in range(2, max_val+1):
        if not is_prime[i] or i * i > max_val:
            continue
        for j in range(i*i, max_val+1, i):
            is_prime[j] = False
    res = []
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            res.append(i)
    return res

def get_prime_factor(n, primes):
    if n == 1:
        return (1, 1)
    res = []
    for p in primes:
        if p * p > n:
            break
        c = 0
        while not n % p:
            n //= p
            c += 1
        if c:
            res.append((p, c))
    if n != 1:
        res.append((n, 1))
    return res

primes = get_primes(1000000)

n=getint()
if n == 1:
    print("1")
    sys.exit(0)

factors = collections.defaultdict(int)
for i in range(2,n+1):
    tmp = get_prime_factor(i,primes)
    for p, c in tmp:
        factors[p] += c

res = 1
for p,c in factors.items():
    res *= c + 1
    res %= 10**9+7

print(res)
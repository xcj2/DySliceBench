from collections import defaultdict
import math

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while b > 0:
        a, b = b, a % b
    return a

def sieve_of_eratosthenes(n):
    sieve = list(range(n+1))
    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if sieve[i] < i:
            continue
        for j in range(i * i, n + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve

def factorize_by_sieve(x, sieve):
    factor = defaultdict(int)
    while sieve[x] != x:
        factor[sieve[x]] += 1
        x //= sieve[x]
    factor[x] += 1
    return factor

n = int(input())
a_list = list(map(int, input().split()))

sieve = sieve_of_eratosthenes(max(a_list))
pairwise = True
setwise = True
primes = set()
x = a_list[0]
for a in a_list:
    x = gcd(x, a)
    if pairwise and a != 1:
        factor = set(factorize_by_sieve(a, sieve).keys())
        pairwise = primes.isdisjoint(factor)
        primes |= factor

if pairwise:
    print("pairwise coprime")
elif x == 1:
    print("setwise coprime")
else:
    print("not coprime")
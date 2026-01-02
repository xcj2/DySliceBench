from collections import defaultdict

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while b > 0:
        a, b = b, a % b
    return a

def sieve_of_eratosthenes(n):
    sieve = [0] * (n+1)
    sieve[0] = 1 #素数でない
    sieve[1] = 1 #素数でない
    for i in range(2, n):
        if sieve[i] == 0:
            for j in range(2, n // i + 1):
                sieve[i * j] = i
    return sieve

def factorize_by_sieve_of_eratosthenes(x, sieve):
    factor = defaultdict(int)
    while sieve[x]:
        factor[sieve[x]] += 1
        x //= sieve[x]
    factor[x] += 1
    return factor

n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()

sieve = sieve_of_eratosthenes(a_list[-1])
pairwise = True
setwise = True
primes = set()
x = a_list[0]
for a in a_list:
    x = gcd(x, a)
    if pairwise and a != 1:
        factor = set(factorize_by_sieve_of_eratosthenes(a, sieve).keys())
        if not primes.isdisjoint(factor):
            pairwise = False
        else:
            primes |= factor

if pairwise:
    print("pairwise coprime")
elif x == 1:
    print("setwise coprime")
else:
    print("not coprime")



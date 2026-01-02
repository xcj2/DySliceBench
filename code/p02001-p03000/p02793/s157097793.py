#  --*-coding:utf-8-*--

MOD = 10**9 + 7

def getPrimes(n):
    if (n < 2):
        return []

    flags = [False]*(n+1)
    primes = [2]

    for p in range(3, n+1, 2):
        if not flags[p]:
            primes.append(p)
            for k in range(p**2, n+1, p):
                flags[k] = True

    return primes


def modPow(a, b, mod):
    x = 1
    
    while b > 0:
        if b & 1:
            x = (x*a)%mod

        a = (a**2)%mod
        b //= 2

    return x


def getModInv(a, b):
    return 1 if (a == 1) else int((1-b*getModInv(b%a, a))/a%b)


def getFactors(x):
    factors = {}
    for p in P:
        if x < 2:
            break

        n = 0
        while x%p == 0:
            x //= p
            n += 1

        if n > 0:
            factors[p] = n

    if x > 1:
        factors[x] = 1

    return factors


P = getPrimes(1000)

N = int(input())
A = list(map(int, input().split()))

maxFacts = {}

for a in A:
    facts = getFactors(a)
    for p in facts:
        if not p in maxFacts or maxFacts[p] < facts[p]:
            maxFacts[p] = facts[p]

lcd = 1
for p in maxFacts:
    lcd = lcd * modPow(p, maxFacts[p], MOD)%MOD

lcd %= MOD

s = 0
for a in A:
    s += lcd*getModInv(a, MOD)%MOD

print(s%MOD)            
            

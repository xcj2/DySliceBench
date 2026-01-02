inpl = lambda: list(map(int,input().split()))

def gcd(a, b):
    if a < 0: a = -a
    if b < 0: b = -b
    while b > 0:
        (a, b) = (b, a % b)
    return a

import math
def primes(N):
    P = []
    for i in range(2,N):
        sieve = 1
        for p in P:
            if p*p > i:
                break
            elif i % p == 0:
                sieve = 0
                break
        if sieve == 0:
            continue
        else:
            P.append(i)
    return P

def factorize(n, P=None):
    if P is None:
        P = primes(int(math.sqrt(n))+1)
    factor = []
    power = []
    for p in P:
        if p * p > n:
            break
        elif n % p == 0:
            k = 0
            while n % p == 0:
                n //= p
                k += 1
            factor.append(p)
            power.append(k)
    if n > 1:
        factor.append(n)
        power.append(1)
    return factor, power

A, B = inpl()
C = gcd(A,B)
factor, _ = factorize(C)
print(len(factor)+1)
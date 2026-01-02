from collections import Counter
from math import gcd

class Prime:
    def __init__(self, N):
        smallestPrime = [1] * (N + 1)
        primes = []

        for i in range(2, N + 1):
            if smallestPrime[i] != 1:
                continue
            primes.append(i)
            for p in range(i * 2, N + 1, i):
                if smallestPrime[p] == 1:
                    smallestPrime[p] = i

        self.smallestPrime = smallestPrime
        self.primes = primes

    def isPrime(self, n):
        return n > 1 and self.smallestPrime[n] == 1

    def factorization(self, n):
        ret = Counter()
        while True:
            p = self.smallestPrime[n]
            if p == 1:
                break
            ret[p] += 1
            n //= p
        if n > 1:
            ret[n] += 1
        return ret

N = int(input())
A = list(map(int, input().split()))
prime = Prime(max(A) + 100)

def isSetwise(A):
    ret = A[0]
    for a in A:
        ret = gcd(ret, a)
    return ret == 1

def isPairwise(A):
    cnt = Counter()
    for a in A:
        for p in prime.factorization(a):
            if cnt[p] >= 1:
                return False
            cnt[p] += 1
    return True

if not isSetwise(A):
    print('not coprime')
elif isPairwise(A):
    print('pairwise coprime')
else:
    print('setwise coprime')

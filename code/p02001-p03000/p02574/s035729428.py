from functools import reduce
from collections import defaultdict
import sys
import math

input = sys.stdin.readline

# 素因数分解O(√n)


def primeFactor(n):
    res = defaultdict(lambda: 0)
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            res[i] += 1
            n = n // i
    if n != 1:
        res[n] = 1
    return res


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    primes = defaultdict(lambda: 0)
    setp = True
    pairs = True
    if gcd(*A) != 1:
        setp = False
        pairs = False
    else:
        for i in range(N):
            pf = primeFactor(A[i])
            for k in pf.keys():
                primes[k] += 1
                if primes[k] != 1:
                    pairs = False
            if not pairs:
                break
    if pairs:
        print('pairwise coprime')
    elif setp:
        print('setwise coprime')
    else:
        print('not coprime')


if __name__ == '__main__':
    main()

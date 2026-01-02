import sys
from math import gcd

input = sys.stdin.buffer.readline


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return (i for i in range(n + 1) if is_prime[i])


N = int(input())
A = tuple(map(int, input().split()))
MAX = 10 ** 6


def pairwise(A):
    table = [0] * (10 ** 6 + 1)
    for a in A:
        table[a] += 1
    for p in primes(MAX):
        ct = 0
        for i in range(p, MAX + 1, p):
            ct += table[i]
        if ct > 1:
            return False
    return True


def setwise(A):
    g = A[0]
    for a in A:
        g = gcd(a, g)
    return g == 1


if pairwise(A):
    print('pairwise coprime')
elif setwise(A):
    print('setwise coprime')
else:
    print('not coprime')

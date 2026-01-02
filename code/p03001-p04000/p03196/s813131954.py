# 46
from collections import Counter
import sys
import math


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


def prime_factrize(n):
    if n < 2:
        return []
    p_factors = []
    while n % 2 == 0:
        p_factors.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            p_factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        p_factors.append(n)
    return p_factors


# 素因数とその個数のタプルのリストを返す
def get_prime_counts(n):
    p_factors = prime_factrize(n)
    counter = Counter(p_factors)
    return list(counter.items())


def main():
    n, p = LI()
    primes = get_prime_counts(p)
    ans = 1
    for base, exp in primes:
        if exp >= n:
            ans *= base ** (exp // n)
    print(ans)


main()

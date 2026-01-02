#!/usr/bin/env python3

def gcd(m, n):
    if m < n:
        return gcd(n, m)
    if m % n == 0:
        return n
    return gcd(n, m % n)


def primeFactorize(n):
    primes = set()
    d = 2
    while d*d <= n:
        while n % d == 0:
            primes.add(d)
            n = n // d
        d += 1
    if n > 1:
        primes.add(n)
    return primes


def solve(A, B):
    primes = primeFactorize(gcd(A, B))
    return len(primes) + 1


if __name__ == '__main__':

    A, B = map(int, input().split())

    ans = solve(A, B)

    print(ans)

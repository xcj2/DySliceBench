#!/usr/bin/env python3
import sys
import math


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def generate_primes(n):
    if n < 2:
        return []
    is_prime_array = [True] * (n + 1)
    is_prime_array[0], is_prime_array[1] = False, False
    for i in range(2, n+1):
        if is_prime_array[i]:
            k = 2 * i
            while k < n + 1:
                is_prime_array[k] = False
                k += i
    return list(filter(lambda i: is_prime_array[i], range(n+1)))


def main():
    N = II()
    if N <= 1:
        print(0)
        exit()
    max_prime = math.ceil(N**0.5)
    primes = generate_primes(max_prime)
    es = [0] * len(primes)
    for i in range(len(primes)):
        while N % primes[i] == 0:
            N /= primes[i]
            es[i] += 1

    ans = 0
    if int(N) != 1:
        ans += 1

    for i in range(len(es)):
        k = 1
        while es[i] - k >= 0:
            es[i] -= k
            k += 1
            ans += 1

    print(ans)


main()

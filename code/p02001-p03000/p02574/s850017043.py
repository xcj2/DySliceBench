#!/usr/bin/env python3


import collections
import functools
from math import gcd


L = 10 ** 6 + 1


def sieve_of_eratosthenes(end):
    """Enumerates prime numbers below the given integer `end`.

    Returns (as a tuple):

    - `is_prime`: a list of bool values.
      If an integer `i` is a prime number, then `is_prime[i]` is True.
      Otherwise `is_prime[i]` is False.
    - `primes`: a list of prime numbers below `end`.
    """

    if end <= 1:
        raise ValueError("The integer `end` must be greater than one")
    is_prime = [True for _ in range(end)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False
    return primes


PRIMES = sieve_of_eratosthenes(L)


def factorize(n):
    factors = []
    if n < 2:
        return factors
    for p in PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors


def is_pairwise_coprime(bs):
    lcm_fs = set()
    for b in bs:
        ps = set(factorize(b))
        for p in ps:
            if p in lcm_fs:
                return False
            else:
                lcm_fs.add(p)
    return True


def is_setwise_coprime(bs):
    return functools.reduce(gcd, bs) == 1


def main():
    n = int(input())
    bs = [int(b) for b in input().split()]
    if is_pairwise_coprime(bs):
        print("pairwise coprime")
    elif is_setwise_coprime(bs):
        print("setwise coprime")
    else:
        print("not coprime")


if __name__ == '__main__':
    main()
#!/usr/bin/env python3


import array
import collections
import math


def sieve_of_eratosthenes(end, typecode="L"):
    assert end > 1
    is_prime = array.array("B", (True for i in range(end)))
    is_prime[0] = False
    is_prime[1] = False
    primes = array.array(typecode)
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False
    return primes


def factorize_trial_division(n, typecode="Q"):
    factors = array.array(typecode)
    if n < 2:
        return factors
    for p in sieve_of_eratosthenes(math.ceil(math.sqrt(n)) + 1):
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors


def solve(n, p):
    factors_counter = collections.Counter(factorize_trial_division(p))
    res = 1
    for k, v in factors_counter.most_common():
        d = v // n
        if d == 0:
            break
        else:
            res *= k ** d
    return res


def main():
    n, p = (int(z) for z in input().split())
    print(solve(n, p))


if __name__ == "__main__":
    main()
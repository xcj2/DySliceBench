#!/usr/bin/env python3

import array


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


def solve(x):
    primes = sieve_of_eratosthenes(x * 5)
    for p in primes:
        if x <= p:
            return p


def main():
    x = int(input())
    p = solve(x)
    print(p)


if __name__ == "__main__":
    main()

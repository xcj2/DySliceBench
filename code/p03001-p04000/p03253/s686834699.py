#!/usr/bin/env python3


import array
import collections
import functools
import itertools
import math
import random


M = 10 ** 9 + 7


def sieve_of_eratosthenes(end, typecode="L"):
    """Enumerates the prime numbers below the given integer.
    :param int end: Prime numbers below this integer will be enumerated.
    :param str typecode: The type of the array to be returned (optional).
    :return: The array of the prime numbers.
    :rtype: :class:`array.array`
    """

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


def factorize_trial_division(n, typecode="L"):
    """Factorizes the given integer in prime numbers by trial division.
    :param int n: The integer to be factorized.
    :param str typecode: The type of the array to be returned (optional).
    :return: The array of factors.
    :rtype: :class:`array.array`
    """
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


def is_prime_miller_rabin(n, k=50):
    """Determing whether the given integer is prime by the Miller-Rabin test.
    :param int n: The integer to be checked.
    :param int k: The parameter representing the accuracy of the determination.
    :return: Whether n is prime or not.
    :rtype: bool
    """
    assert n > 0
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(1, n - 1)
        if pow(a, d, n) != 1:
            for r in range(0, s):
                if pow(a, d * 2 ** r, n) == n - 1:
                    break
            else:
                return False
    return True


class ModPrime(object):

    def __init__(self, max_n=500000, mod=M):
        # cf. http://hos.ac/slides/20130319_enumeration.pdf
        self.max_n = max_n
        assert is_prime_miller_rabin(mod)
        self.mod = mod
        self.invs = [None, 1]
        for i in range(2, self.max_n + 1):
            self.invs.append(mod - mod // i * self.invs[mod % i] % mod)
        self.facts = [1]
        self.fact_invs = [1]
        for i in range(1, self.max_n + 1):
            self.facts.append(self.facts[i - 1] * i % mod)
            self.fact_invs.append(self.fact_invs[i - 1] * self.invs[i] % mod)
    
    def inv(self, n):
        return self.invs[n]
    
    def fact(self, n):
        return self.facts[n]
    
    def fact_inv(self, n):
        return self.fact_invs[n]
    
    def comb(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact(n) * self.fact_inv(r) % self.mod * self.fact_inv(n - r) % self.mod
    
    def multi_choose(self, n, r):
        return self.comb(n + r - 1, r)


def mod_prod(ys, mod=M):
    xs = itertools.chain((1, ), ys)
    return functools.reduce(lambda x, y: x * y % mod, xs) % mod


def solve(n, m, mod=M):
    fs = collections.Counter(factorize_trial_division(m))
    mp = ModPrime(mod=M)
    res = mod_prod((mp.multi_choose(n, v) for v in fs.values()), mod=M)
    return res


def main():
    n, m = (int(z) for z in input().split())
    res = solve(n, m)
    print(res)

if __name__ == '__main__':
    main()
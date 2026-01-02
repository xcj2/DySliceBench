import math
import unittest
import sys


class PrimeFactorization:
    def __init__(self, upper_limit):
        _primes, minimam_prime_factor = PrimeFactorization.list_primes(
            upper_limit)
        self.minimam_prime_factor = minimam_prime_factor

    def list_primes(upper_limit):
        # Sieve of Eratosthenes
        minimam_prime_factor = [i for i in range(upper_limit)]
        if upper_limit <= 2:
            return [], [0, 1]

        is_prime = [True] * upper_limit
        sqrt_upper_limit = int(upper_limit**0.5+1)
        for i in range(2, sqrt_upper_limit):
            if not is_prime[i]:
                continue
            minimam_prime_factor[i] = i
            for j in range(i*i, upper_limit, i):
                is_prime[j] = False
                if minimam_prime_factor[j] == j:
                    minimam_prime_factor[j] = i
        primes = [2]
        for i in range(3, upper_limit, 2):
            if is_prime[i]:
                minimam_prime_factor[i] = i
                primes.append(i)
        return primes, minimam_prime_factor

    def list_prime_factors(self, n) -> set:
        factors = set()
        while 1 < n:
            factors.add(self.minimam_prime_factor[n])
            n //= self.minimam_prime_factor[n]
        return factors


class TestPrimeFactorization(unittest.TestCase):
    def test(self):
        primes, minimam_prime_factor = PrimeFactorization.list_primes(20)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(minimam_prime_factor, [
                         0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19])


def is_pairwise_coprime(n, a):
    pf = PrimeFactorization(max(a)+1)
    e = set()
    for ai in a:
        e2 = pf.list_prime_factors(ai)
        if e & e2:
            return False
        e |= e2
    return True


def is_setwise_coprime(n, a):
    gcd = a[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i])
        if gcd == 1:
            return True
    return gcd == 1


def solve(n, a):
    if is_pairwise_coprime(n, a):
        return 'pairwise coprime'
    elif is_setwise_coprime(n, a):
        return 'setwise coprime'
    else:
        return 'not coprime'


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == "__main__":
    main()


PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
    59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
    131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
    389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
    479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
    587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
    673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769,
    773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
    881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
    991, 997, 1009
]


class Test(unittest.TestCase):
    def test_1(self):
        n = 3
        a = [3, 4, 5]
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_2(self):
        n = 3
        a = [6, 10, 15]
        self.assertEqual(is_pairwise_coprime(n, a), False)
        self.assertEqual(is_setwise_coprime(n, a), True)
        self.assertEqual(solve(n, a), 'setwise coprime')

    def test_3(self):
        n = 3
        a = [6, 10, 16]
        self.assertEqual(solve(n, a), 'not coprime')

    def test_4(self):
        n = 3
        a = [1, 1, 1]
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_5(self):
        n = 3
        a = [1, 2, 2]
        self.assertEqual(solve(n, a), 'setwise coprime')

    def test_6(self):
        n = 10
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_7(self):
        n = 11
        a = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_8(self):
        n = 2
        a = [1, 1]
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_9(self):
        n = 2
        a = [1, 2]
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_10(self):
        n = 2
        a = [10**6, 10**6-1]
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_11(self):
        n = 3
        a = [10**6, 10**6-1, 10**6, ]
        self.assertEqual(solve(n, a), 'setwise coprime')

    def test_12(self):
        n = len(PRIMES) * 2
        a = PRIMES + PRIMES
        self.assertEqual(solve(n, a), 'setwise coprime')

    def test_13(self):
        a = [997, 1009, 1013, 1019, 1021, 1031, 1033, 1039,
             1049, 1051, 1061, 1063, 1069, 1087, ]
        n = len(a)
        self.assertEqual(solve(n, a), 'pairwise coprime')

    def test_14(self):
        a = [1009*2, 1013*3, 1019*5, 1021, 1031, 1033, 1039,
             1049, 1051, 1061, 1063, 1069, 1087, ]
        n = len(a)
        self.assertEqual(solve(n, a), 'pairwise coprime')

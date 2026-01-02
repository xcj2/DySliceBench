from collections import defaultdict
from itertools import chain


def gcd(a, b):
    # 最大公約数
    while b:
        a, b = b, a % b
    return a


def fast_prime_set(n):
    # nまでの素数リスト高速版 setで返す
    # chainの読み込みが必要！
    if n < 4:
        return ({}, {}, {2}, {2, 3})[n]
    n_sqrt = int(n ** 0.5) + 1
    primes = {2, 3} | set(chain(range(5, n + 1, 6), range(7, n + 1, 6)))
    for i in range(5, n_sqrt, 2):
        if i in primes:
            primes.difference_update(range(i * i, n, i * 2))
    return primes


def prime_factorization(x):
    # 素因数分解
    # 事前に素数のセットが必要
    primes = fast_prime_set(10 ** 6)

    fact = defaultdict(int)
    for prime in primes:
        while x % prime == 0:
            fact[prime] += 1
            x //= prime
        if x == 1:
            break
        if x in primes:
            fact[x] += 1
            break
    if x!= 1:
        fact[x] = 1
    return fact


if __name__ == '__main__':
    a, b = map(int, input().split())
    gcd_a_b = gcd(a, b)
    prime_fact = prime_factorization(gcd_a_b)
    print(1 + len(prime_fact))
from collections import defaultdict


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    # a <= b
    if a == 0:
        return b
    else:
        r = b % a
        return gcd(r, a)


def prime_factorization(n):
    factors = defaultdict(int)
    i = 1
    n_sub = n
    while True:
        i += 1
        if i * i > n or n_sub == 1:
            break

        while n_sub % i == 0:
            n_sub = n_sub // i
            factors[i] += 1

    if n_sub != 1:
        factors[n_sub] = 1
    return factors


def main():
    a, b = map(int, input().split())
    g = gcd(a, b)
    if g == 1:
        return 1
    primes = prime_factorization(g)
    # add "1"
    return len(primes) + 1
    

print(main())

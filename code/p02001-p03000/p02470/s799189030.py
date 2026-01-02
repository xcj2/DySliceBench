from itertools import takewhile
from functools import reduce


def gen_prime_candidates():
    yield 2
    yield 3
    n = 0
    while 1:
        yield n + 5
        yield n + 7
        n += 6


def calc_exp(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n /= p
    return e, n


def factorize(n):
    f = ()
    for p in takewhile(lambda p: p * p <= n, gen_prime_candidates()):
        e, n = calc_exp(n, p)
        if e:
            f += (p, )
    if n > 1:
        f += (n, )
    return f


def phi(n):
    return reduce(lambda x, p: x * (p-1) / p, factorize(n), n)


n = int(input())
print(int(phi(n)))


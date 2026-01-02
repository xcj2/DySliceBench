from functools import reduce

prime = 1000000007


def modpow(a: int, n: int, mod: int = prime) -> int:
    res = 1
    while n > 0:
        if n & 1 != 0:
            res = res * a % mod
        a = a * a % mod
        n = n // 2
    return res


def modinv(a: int, mod: int = prime) -> int:
    return modpow(a, mod-2, mod)


def modfactrial(n: int, mod: int = prime) -> int:
    return reduce(lambda x, y: (x*y) % mod, range(1, n+1), 1)


def modcombination(n: int, r: int, mod: int = prime) -> int:
    # nCr = n!/(r!(n-r)!)
    n_fact = modfactrial(n, mod)
    r_fact = modfactrial(r, mod)
    nr_fact = modfactrial(n-r, mod)
    r_fact_inv = modinv(r_fact, mod)
    nr_fact_inv = modinv(nr_fact, mod)
    return n_fact * r_fact_inv * nr_fact_inv % mod


def abort():
    import sys
    print(0)
    sys.exit(0)


x, y = [int(x) for x in input().split()]
if (2*x-y) % 3 != 0:
    abort()
if (2*y-x) % 3 != 0:
    abort()
n = (2*y-x)//3
m = (2*x-y)//3

if n < 0 or m < 0:
    abort()
print(modcombination(n+m, n))
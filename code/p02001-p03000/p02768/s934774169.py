#!/usr/bin/env python3

import sys

def read_int_list(sep = " "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    return
    print(*args, **kwargs)


def choose(a, b, mod):
    numer, denomi = 1, 1 
    for i in range(0, b):
        denomi = (denomi * (i + 1)) % mod
        numer = ((a - i) * numer) % mod
    return (numer * pow(denomi, mod - 2, mod)) % mod


def main():
    mod = 1000000007
    n, a, b = read_int_list()
    ans = pow(2, n, mod)
    ans = (ans - 1) % mod  # case for zero flowers
    ans = (ans - choose(n, a, mod)) % mod
    ans = (ans - choose(n, b, mod)) % mod
    print(ans)


if __name__ == "__main__":
    main()
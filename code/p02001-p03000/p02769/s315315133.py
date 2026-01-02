#!/usr/bin/env python3

import sys


def read_int_list(sep=" "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    return
    print(*args, **kwargs)


facto = None
ifacto = None

def precompute_facto(n, mod):
    global facto, ifacto
    facto = [1] * (n + 1)
    for i in range(1, n + 1):
        facto[i] = (facto[i - 1] * i) % mod
    ifacto = [1] * (n + 1)
    ifacto[n] = mod_inv(1, facto[n], mod)
    for i in range(0, n):
        p = n - i
        ifacto[p - 1] = ifacto[p] * p % mod


def mod_inv(a, b, mod):
    return (a * pow(b, mod - 2, mod)) % mod


def choose(a, b, mod):
    return facto[a] * ifacto[a - b] % mod * ifacto[b] % mod


def multi_choose(a, b, mod):
    return choose(a + b - 1, b, mod)


def main():
    mod = 1000000007
    n, k = read_int_list()
    precompute_facto(n, mod)
    ans = 0
    for i in range(0, min(k, n - 1) + 1):
        ans = (ans + choose(n, i, mod) * multi_choose(n - i, i, mod)) % mod
    print(ans)


if __name__ == "__main__":
    main()

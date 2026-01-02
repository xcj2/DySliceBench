#!/usr/bin/env python3

import sys

DEBUG = False


def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep=" "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


MOD = int(1e9 + 7)


def mod_inv(a, b, mod):
    return (a * pow(b, mod - 2, mod)) % mod


def solve(as_):
    all_sum = 0
    for a in as_:
        all_sum = (all_sum + a) % MOD
    ans_x2 = 0
    for i in range(0, len(as_)):
        ans_x2 = (
            ans_x2 + ((MOD + (all_sum - as_[i]) % MOD) % MOD) * as_[i] % MOD) % MOD

    return mod_inv(ans_x2, 2, MOD)


def main():
    _n = read(int)
    as_ = read_list(int)
    print(solve(as_))


if __name__ == "__main__":
    main()

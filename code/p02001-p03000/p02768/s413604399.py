#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def get_fraction_mod(numerator, denominator):
    '''
        returns numerator / denominator (mod MOD)
    '''
    inv = pow(denominator, MOD - 2, MOD)
    return numerator * inv % MOD

def make_comb(n, k):
    a = 1
    b = 1
    for i in range(k):
        a = a * (n - i) % MOD
        b = b * (i + 1) % MOD
    ret = get_fraction_mod(a, b)
    return ret


def solve(n: int, a: int, b: int):
    ret = (pow(2, n, MOD) - 1) % MOD
    ret = ret + MOD - make_comb(n, a)
    ret = ret + MOD - make_comb(n, b)
    ret %= MOD
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(n, a, b)

if __name__ == '__main__':
    main()

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
    k = min(k, n - k)
    a = 1
    b = 1
    for i in range(k):
        a = a * (n - i) % MOD
        b = b * (i + 1) % MOD
    ret = get_fraction_mod(a, b)
    return ret

def make_facts(n):
    '''
        make factorials
        0!(=1), 1!, 2!, 3! .... n!
    '''
    fact = [1]
    for i in range(n):
        fact.append((fact[i] * (i + 1)) % MOD)
    return fact


def make_combs(n, k):
    '''
        make [C(n, 0), C(n, 1), C(n, 2) ..... C(n, k)]
        n! / (n - k)! k!
    '''
    facts = make_facts(n)
    invs = [] # inverted for fraction
    for fact in facts:
        invs.append(pow(fact, MOD - 2, MOD))

    ret = []
    for i in range(0, n + 1):
        a = facts[n]
        ret.append(a * invs[i] * invs[n - i] % MOD)
    return ret

def _solve(n):
    dp = [0] * (n + 1)

def solve(n: int, k: int):
    ret = make_comb(n * 2 - 1, n)
    if k < n - 1:
        combs = make_combs(n - 1, n - 1)
        n_combs = make_combs(n, n)
        for i in range(k + 1, n):
            #tmp = make_comb(n, i)
            tmp = n_combs[i]
            t = combs[n - i - 1]
            ret -= tmp * t
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
    k = int(next(tokens))  # type: int
    solve(n, k)

if __name__ == '__main__':
    main()

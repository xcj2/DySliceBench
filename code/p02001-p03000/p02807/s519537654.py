#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def get_fraction_mod(numerator, denominator):
    '''
        returns numerator / denominator (mod 1000000007)
    '''
    inv = pow(denominator, MOD - 2, MOD)
    return numerator * inv % MOD

def make_facts(n):
    '''
        0!(=1), 1!, 2!, 3! .... n!
    '''
    fact = [1]
    for i in range(n):
        fact.append((fact[i] * (i + 1)) % MOD)
    return fact

def solve(N: int, x: "List[int]"):
    facts = make_facts(N)
    f = facts[N - 1]
    ret = 0
    cur = 0
    for i in range(N - 1):
            d = x[i + 1] - x[i]
            cur += get_fraction_mod(f, i + 1)
            tmp  = d * cur
            ret += tmp
            ret %= MOD
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x)

if __name__ == '__main__':
    main()

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

def make_facts(n):
    '''
        make factorials
        0!(=1), 1!, 2!, 3! .... n!
    '''
    fact = [1]
    for i in range(n):
        fact.append((fact[i] * (i + 1)) % MOD)
    return fact

def make_combs_(n, k):
    '''
        make [C(0, k), C(1, k), C(2, k) ..... C(n, k)]
    '''
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    ret = [0] * (n + 1)
    for i in range(k, n + 1):
        a = fact[i]
        b = (fact[k] * fact[i - k]) % MOD
        ret[i] = get_fraction_mod(a, b)
    return ret

def solve(N: int, K: int, A: "List[int]"):
    A.sort()
    combs = make_combs_(N, K - 1)
    mins = 0
    maxs = 0
    for i in range(N):
        mins += combs[N - i - 1] * A[i]
        mins %= MOD
        maxs += combs[i] * A[i]
        maxs %= MOD
    ret = maxs - mins
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
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()

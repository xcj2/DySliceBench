#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 998244353  # type: int

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
        #b = facts[i]
        #c = facts[n - i]
        ret.append(a * invs[i] * invs[n - i] % MOD)
    return ret

def solve(N: int, M: int, K: int):
    pows = []
    for i in range(N + 1):
        t = pow(M - 1, i, MOD)
        pows.append(t)
    s = pow(M, N, MOD)
    #s = pows[N]
    coms = make_combs(N - 1, N - 1)
    #print(s, coms)
    for i in range(K + 1, N):
        c = coms[i]
        ss = M * pows[N - i - 1]
        #print(i, c, ss, c * ss)
        s -= c * ss
        s %= MOD
    print(s)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, M, K)

if __name__ == '__main__':
    main()

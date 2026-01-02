#!/usr/bin/env python3

import sys, math
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int
def calc_fraction_mod(numerator, denominator):
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


def make_combs(n, k):
    '''
        make [C(n - k, 0), C(n - k + 1, 1), C(n, 2) ..... C(n, k)]
    '''
    facts = make_facts(n)
    invs = [] # inverted for fraction
    for fact in facts:
        invs.append(pow(fact, MOD - 2, MOD))

    ret = []
    for i in range(0, k + 1):
        x = n - k + i
        a = facts[x]
        #b = facts[i]
        #c = facts[n - i]
        #ret.append(calc_fraction_mod(a, b))
        ret.append(a * invs[i] * invs[x - i] % MOD)
    return ret

def solve(K: int, S: str):
    n = len(S)
    N = K + n
    ret = 0
    p26 = [1]
    p25 = [1]
    for i in range(1, K + 1):
        #p26.append(pow(26, i, MOD))
        #p25.append(pow(25, i, MOD))
        p26.append(p26[-1] * 26 % MOD)
        p25.append(p25[-1] * 25 % MOD)
    coms = make_combs(N - 1, K)
    #print('a')
    #print('b')
    for i in range(K + 1):
        #tmp = p26[i] * p25[K - i] * c(N - i - 1, K - i)
        tmp = p26[i] * p25[K - i] * coms[K - i]
        #print(i, p26[i], p25[K - i], coms[K - i], tmp)
        ret += tmp
        ret %= MOD
    print(ret)
    return


def solve_(K: int, S: str):
    n = len(S)
    N = K + n
    coms = make_combs(N, n)
    ret = pow(26, N, MOD)
    tmp = pow(25, coms[n], MOD)
    print(coms[n], ret, tmp)
    ret -= tmp
    #ret *= coms[n]
    ret %= MOD
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(K, S)

if __name__ == '__main__':
    main()

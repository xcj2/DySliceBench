#!/usr/bin/env python3

import sys
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
        make [C(0, k), C(1, k), C(2, k) ..... C(n, k)]
    '''
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    ret = [0] * (n + 1)
    for i in range(k, n + 1):
        a = fact[i]
        b = (fact[k] * fact[i - k]) % MOD
        ret[i] = calc_fraction_mod(a, b)
    return ret


def solve(r: "List[int]", c: "List[int]"):
    #t = make_combs_(10, 2)
    ret = 0
    x = make_combs(r[1] + c[1] + 2, r[1])
    y = make_combs(r[0] + c[1] + 2, r[0] - 1)
    for i in range(c[0], c[1] + 1):
        ret += x[r[1] + i + 1]
        ret -= y[r[0] + i]
        ret %= MOD
    print(ret)
    return ret
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = [int()] * (2)  # type: "List[int]"
    c = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(r, c)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def get_factors(n):
    fact = 2
    tmp = n
    ret = []
    while fact * fact <= n:
        count = 0
        while tmp % fact == 0:
            tmp //= fact
            count += 1
        if count > 0:
            ret.append(count)
            #print(fact)
        fact += 1
    if tmp > 1:
        ret.append(1)
    return ret

def comb(n, k):
    if k > n:
        return 0
    ret = 1
    k = min(k, n - k)
    for i in range(k):
        ret *= n - i
        ret //= i + 1
    return ret

def solve(N: int, M: int):
    facts = get_factors(M)
    #print(facts)
    ret = 1
    for c in facts:
        ret *= comb(c + N - 1, N - 1)
    print(ret % MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()

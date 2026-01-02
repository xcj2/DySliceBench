# -*- coding: utf-8 -*-
"""
D - Disjoint Set of Common Divisors
https://atcoder.jp/contests/abc142/tasks/abc142_d

"""
import sys


from collections import defaultdict

def prime_factor(N):
    factors = defaultdict(int)
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            factors[i] += 1
            N //= i
    if N != 1:
        factors[N] = 1

    return factors

def solve(A, B):
    pA = prime_factor(A)
    pB = prime_factor(B)
    res = [1]
    for k in pA.keys():
        if k in pB:
            res.append(k)
    return len(res)


def main(args):
    A, B = map(int, input().split())
    ans = solve(A, B)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])

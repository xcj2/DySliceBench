# -*- coding: utf-8 -*-
"""
C - Factors of Factorial
https://atcoder.jp/contests/arc067/tasks/arc067_a

"""
import sys



from collections import Counter

def prime_factor(N):
    factors = Counter()
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            factors[i] += 1
            N //= i
    if N != 1:
        factors[N] = 1
    return factors


def solve(N):
    f = Counter()
    for i in range(1, N+1):
        f += prime_factor(i)

    MOD = 10**9 + 7
    ans = 1
    for k, v in f.items():
        ans = ans * (v+1) % MOD
    return ans


def main(args):
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
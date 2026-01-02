#!/usr/bin/env python3
import sys
from collections import Counter
import math
MOD = 1000000007  # type: int


def factorial(n):
    prime_count = Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1

    return prime_count


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % MOD
    elif y % 2 == 0:
        return power(x, y//2)**2 % MOD
    else:
        return power(x, y//2)**2 * x % MOD


def div(a, b):
    return (a * power(b, MOD-2)) % MOD


def solve(N: int, A: "List[int]"):

    lcm = Counter()
    for a in A:
        c = factorial(a)
        for k in c:
            lcm[k] = max(c[k], lcm[k])
    # print(lcm)

    LCM = 1
    for k, v in lcm.items():
        LCM *= power(k, v)
        LCM %= MOD
    # print(LCM)

    tot = 0
    for a in A:
        tot += div(LCM, a)
    print(tot % MOD)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()

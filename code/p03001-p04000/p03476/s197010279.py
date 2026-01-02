#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    q, = read_h()
    rng = read_v(q, m=2)

    MAX = 100000

    # Sieve of Eratosthenes
    is_prime = [True] * MAX
    is_prime[0], is_prime[1] = False, False
    for i in range(MAX):
        if not is_prime[i]:
            continue
        for j in range(i * 2, MAX, i):
            is_prime[j] = False

    # Find 2017-like numbers
    a = [0] * (MAX + 1)
    for i in range(MAX + 1):
        if i % 2 == 0:
            continue
        if is_prime[i] and is_prime[(i + 1) // 2]:
            a[i] = 1

    # Calc cumulative sum
    s = [0] * (MAX + 1)
    for i in range(MAX):
        s[i + 1] = s[i] + a[i]

    # Print answers
    for l, r in rng:
        print(s[r + 1] - s[l])


if __name__ == '__main__':
    main()

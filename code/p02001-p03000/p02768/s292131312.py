#!/usr/bin/env pypy3


P = 10 ** 9 + 7


def binom(n, k, p=P):
    denominator = 1
    for i in range(2, k + 1):
        denominator *= i
        denominator %= p
    numerator = 1
    for i in range(n, n - k, -1):
        numerator *= i
        numerator %= p
    inv_denominator = pow(denominator, p - 2, p)
    res = numerator * inv_denominator % p
    return res


def compute(n, a, b, p=P):
    num_all = pow(2, n, p)
    num_a = binom(n, a, p)
    num_b = binom(n, b, p)
    res = (num_all - 1 - num_a - num_b) % p
    return res


def main():
    n, a, b = (int(z) for z in input().split())
    res = compute(n, a, b)
    print(res)


if __name__ == "__main__":
    main()

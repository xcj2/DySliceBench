#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def cmb(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    if r == 1:
        return n

    numer = [n - r + k + 1 for k in range(r)]
    denom = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denom[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numer[k - offset] /= pivot
                denom[k] /= pivot

    result = 1
    for k in range(r):
        if numer[k] > 1:
            result *= int(numer[k])
            result %= MOD

    return result


def solve(n: int, a: int, b: int):

    ans = pow(2, n, MOD)-1
    ans -= cmb(n, a)
    ans %= MOD
    ans -= cmb(n, b)
    ans %= MOD
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(n, a, b)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")

from collections import Counter


def factorial(n):
    prime_count = Counter()

    for i in range(2, int(n**0.5) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1

    return prime_count


def num_divisors(prime_count):
    num = 1

    for prime, count in prime_count.items():
        num *= (count + 1)

    return num


def divisors(n):
    ret = set()
    for i in range(1, int(n ** 0.5) + 1):
        d, m = divmod(n, i)
        if m == 0:
            ret.add(i)
            ret.add(d)
    return sorted(ret)


def solve(N: int):

    f = factorial(N-1)
    ans = num_divisors(f)-1

    divs = divisors(N)
    for k in divs:
        if k == 1:
            continue
        n = N
        while n % k == 0:
            n = n//k
            if n == 1:
                break
        if n % k == 1:
            ans += 1
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()

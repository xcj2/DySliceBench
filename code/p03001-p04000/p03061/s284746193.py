#!/usr/bin/env python3
import sys
import math
from collections import Counter
import collections
INF = float("inf")


def factorial(n):
    # 試し割りによる素因数分解
    prime_count = collections.Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1

    return prime_count


def GCD(a, b):
    if a == 0:
        return b
    else:
        return GCD(b % a, a)


def GCDs(*a):
    # リストで入力しないよう注意。
    if len(a) == 0:
        return -1  # エラー

    if len(a) == 1:
        return a[0]

    res = a[0]
    for i in range(1, len(a)):
        res = GCD(res, a[i])
    return res


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def solve(N: int, A: "List[int]"):

    asc = [0]
    for i in range(N):
        asc.append(GCD(asc[-1], A[i]))
    desc = [0]
    for i in range(N):
        desc.append(GCD(desc[-1], A[N-i-1]))

    buf = []
    for i in range(N):
        buf.append(GCD(asc[i], desc[N-i-1]))
    print(max(buf))

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

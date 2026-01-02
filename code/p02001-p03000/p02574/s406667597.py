import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict
from functools import lru_cache


@lru_cache(None)
def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x, y = y, r
    return x


def merge_dict(d1, d2):
    for k, v in d2.items():
        d1[k] += v
    return d1


def input():
    return sys.stdin.readline().strip()


def gen_prime_table(last: int, first=2) -> list:
    if last < 1:
        return [None]
    elif last < 2:
        return [None, None]
    table = [None] * (last + 1)

    for i in range(first, last + 1):
        if not table[i]:
            table[i] = i
            for j in range(i * 2, last + 1, i):
                table[j] = i
    return table


def prime_factorization(N: int, min_factor: list) -> dict:
    if N < 2:
        return {1: 1}
    primes = dict()
    primes[1] = 1
    while N != 1:
        p = min_factor[N]
        if p in primes.keys():
            primes[p] += 1
        else:
            primes[p] = 1
        N = N // p
    return primes


def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    primes = defaultdict(int)
    is_pair_gcd = True
    set_gcd = A[0]
    min_factor = gen_prime_table(max(A))  # この部分の計算不可が大きい (n*log_log_n)
    for i in range(n):
        set_gcd = gcd(set_gcd, A[i])
        p = prime_factorization(A[i], min_factor)
        if is_pair_gcd:
            for k, v in p.items():
                if k == 1:
                    continue
                if k in primes.keys():
                    is_pair_gcd = False
                else:
                    primes[k] += v

    if is_pair_gcd:
        print("pairwise coprime")
        return

    if set_gcd == 1:
        print("setwise coprime")
    else:
        print("not coprime")

    return


if __name__ == "__main__":
    main()

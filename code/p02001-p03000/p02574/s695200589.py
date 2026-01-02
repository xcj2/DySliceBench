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


def prime_factorization(N: int) -> dict:
    primes = defaultdict(int)
    primes[1] = 1
    if N < 2:
        return primes
    i = 2
    while i * i <= N:
        while N % i == 0:
            primes[i] += 1
            N = N // i
        i += 1
    if N != 1:
        primes[N] = 1
    return primes


def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    primes = defaultdict(int)
    is_pair_gcd = True
    set_gcd = A[0]
    for i in range(n):
        set_gcd = gcd(set_gcd, A[i])
        if is_pair_gcd:
            p = prime_factorization(A[i])
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

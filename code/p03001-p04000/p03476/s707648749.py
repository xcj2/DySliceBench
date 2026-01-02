import sys
import numpy as np
from itertools import accumulate


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    def make_prime(U):
        is_prime = np.zeros(U, np.bool)
        is_prime[2] = 1
        is_prime[3::2] = 1
        M = int(U ** 0.5) + 1
        for p in range(3, M, 2):
            if is_prime[p]:
                is_prime[p * p :: p + p] = 0
        return is_prime

    primes = make_prime(10 ** 5 + 1)
    check = np.where(primes == True, 1, 0)
    for i in range(1, 10 ** 5 + 1):
        if i % 2 == 1:
            if primes[i]:
                if not primes[(i + 1) // 2]:
                    check[i] = 0
        else:
            continue
    check[2] = 0
    check = list(accumulate(check))
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        print(check[r] - check[l - 1])


if __name__ == "__main__":
    main()

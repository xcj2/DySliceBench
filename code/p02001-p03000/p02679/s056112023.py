#!/usr/bin/env python3
import sys
from math import gcd
from collections import defaultdict
sys.setrecursionlimit(10**8)

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]", B: "List[int]"):

    def quadrant(a, b):
        if a > 0 and b >= 0:
            return 0
        elif a <= 0 and b > 0:
            return 1
        elif a < 0 and b <= 0:
            return 2
        elif a >= 0 and b < 0:
            return 3
        else:
            return None

    def norm(a, b):
        g = gcd(a, b)
        a //= g
        b //= g
        while quadrant(a, b) != 0:
            a, b = -b, a
        return a, b

    d = defaultdict(lambda: [0, 0, 0, 0])
    kodoku = 0
    for i, (a, b) in enumerate(zip(A, B)):
        if (a, b) == (0, 0):
            kodoku += 1
        else:
            d[norm(a, b)][quadrant(a, b)] += 1

    ans = 1
    for v in d.values():
        buf = pow(2, v[0]+v[2], MOD)
        buf += pow(2, v[1]+v[3], MOD)
        buf = (buf-1) % MOD
        ans *= buf
        ans %= MOD

    print((ans-1+kodoku) % MOD)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == '__main__':
    main()

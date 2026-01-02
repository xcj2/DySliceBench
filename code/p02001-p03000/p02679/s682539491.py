#!/usr/bin/env python3
import bisect
import collections
import sys
import math
from fractions import Fraction

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]", B: "List[int]"):
    ab = collections.defaultdict(lambda: [0, 0])  # [posi][nega]
    zeros = 0
    for i in range(N):
        if A[i] == B[i] == 0:
            zeros += 1
        elif A[i] == 0:
            ab[0][1] += 1
        elif B[i] == 0:
            ab[0][0] += 1
        elif A[i] * B[i] >= 0:
            v = math.gcd(A[i], B[i])
            ab[(abs(B[i]) // v, abs(A[i]) // v)][0] += 1
        else:
            v = math.gcd(A[i], B[i])
            ab[(abs(A[i]) // v, abs(B[i]) // v)][1] += 1

    # check B[i] ==0
    ans = 1
    for x, y in ab.values():
        pattern = 1  # not select
        pattern += 2 ** x - 1
        pattern += 2 ** y - 1
        ans = ans * pattern % MOD
    print((ans - 1) % MOD + zeros)

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

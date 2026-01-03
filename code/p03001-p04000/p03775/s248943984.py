#!/usr/bin/env python3
import sys
import math
INF = float("inf")


def divisors_pair(n):
    ret_A = []
    ret_B = []
    for i in range(1, int(n ** 0.5) + 1):
        d, m = divmod(n, i)
        if m == 0:
            ret_A.append(i)
            ret_B.append(d)
    return ret_A, ret_B


def solve(N: int):
    A, B = divisors_pair(N)
    m = INF
    for a, b in zip(A, B):
        curr = max(len(str(a)), len(str(b)))
        m = min(m, curr)
    print(m)
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

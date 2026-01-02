#!/usr/bin/env python3
import sys
import math
INF = float("inf")

MOD = 2  # type: int


def solve(N: int, A: "List[int]"):
    m = INF
    for a in A:
        m = min(m, a & -a)
    print(int(math.log2(m)))
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

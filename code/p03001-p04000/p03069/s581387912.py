#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, S: str):
    stones = [1 if s == "#" else 0 for s in S]
    acc = [0]+list(accumulate(stones))
    counter = 0
    m = INF
    for i in range(N+1):
        m = min(m, (acc[i]) + (N-i-(acc[N]-acc[i])))
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, a: "List[int]"):
    acc = list(accumulate(a))
    m = INF
    for i in range(N-1):
        buf = abs(acc[i]-(acc[N-1]-acc[i]))
        m = min(m, buf)
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()

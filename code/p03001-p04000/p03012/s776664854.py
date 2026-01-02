#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, W: "List[int]"):
    Wacc = list(accumulate(W))
    m = INF
    for i in range(N):
        buf = abs(Wacc[i]-(Wacc[N-1]-Wacc[i]))
        if m > buf:
            m = buf
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, W)


if __name__ == '__main__':
    main()

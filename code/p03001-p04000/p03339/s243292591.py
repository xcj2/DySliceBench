#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, S: str):
    ss = [1 if c == "E" else 0 for c in S]
    ss = list(accumulate(ss))

    mi, m = -1, INF
    for i in range(N):
        b = 0
        if i - 1 >= 0:
            b += i - ss[i-1]
        if i+1 <= N-1:
            b += ss[N-1]-ss[i]
        # print(i, b)
        if b < m:
            m = b
            mi = i
    print(m)
    # print(mi)

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

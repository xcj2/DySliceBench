#!/usr/bin/env python3
import sys
from bisect import bisect_left
INF = float("inf")


def solve(N: int, H: "List[int]"):
    mc = 0
    counter = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            counter += 1
        else:
            if counter > mc:
                mc = counter
            counter = 0
    if counter > mc:
        mc = counter
    print(mc)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, H)


if __name__ == '__main__':
    main()

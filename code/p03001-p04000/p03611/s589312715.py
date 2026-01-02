#!/usr/bin/env python3
import sys
from bisect import bisect_left
INF = float("inf")


def solve(N: int, a: "List[int]"):
    a.sort()
    lower, upper = 0, 2
    m = 1
    while lower < 10**5:
        m = max(m, bisect_left(a, upper+1)-bisect_left(a, lower))
        lower += 1
        upper += 1
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

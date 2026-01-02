#!/usr/bin/env python3
import sys
import math
import bisect
INF = float("inf")


def solve(N: int):

    if N == 1:
        print(0)
        return
    count = 0
    for r in range(1, int(math.sqrt(N))+1):  # 商
        # 余りは二分探索で良い
        lower = -(-N//r+1)
        upper = N//r
        while lower + 1 < upper:
            mid = (lower+upper)//2
            if N % mid >= r:
                lower = mid
            else:
                upper = mid
        if N % lower == r:
            count += lower
    print(count)

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

#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(X: int, Y: int):

    if Y%2:
        print(NO)
        return
    a = Y//2 - X
    if X- a < 0:
        print(NO)
        return
    if  a < 0:
        print(NO)
        return
    print(YES
          )
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)

if __name__ == '__main__':
    main()

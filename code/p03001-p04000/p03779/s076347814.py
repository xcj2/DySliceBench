#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(X: int):

    def isOK(m):
        return X <= m*(m+1)/2

    ng = -1
    ok = X

    while abs(ok - ng) > 1:
        mid = (ok + ng)//2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(K: int):

    X = set()

    def rec(keta, x):
        X.add(x)
        if keta == 10:
            return
        y = x % 10
        if 0 <= y - 1:
            rec(keta+1, x*10 + y-1)
        rec(keta+1, x*10+y)
        if y+1 <= 9:
            rec(keta+1, x*10+y+1)

    for i in range(1, 10):
        rec(1, i)
    X = sorted(X)
    print(X[K-1])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == '__main__':
    main()

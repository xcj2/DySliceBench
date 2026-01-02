#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(K: int):

    X = set()

    def rec(keta, val):
        X.add(val)
        if keta == 10:
            return

        for j in range(-1, 2):
            add = (val % 10)+j
            if add >= 0 and add <= 9:
                rec(keta+1, val*10+add)

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

#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(X: int):
    prices = [100, 101, 102, 103, 104, 105]
    flag = [None]*(100000+1)
    flag[0] = True

    def rec(x):
        if flag[x] is not None:
            return flag[x]

        if x < 100:
            flag[x] = False
            return False

        fff = False
        for p in prices:
            fff = fff or rec(x-p)
            if fff == True:
                break
        flag[x] = fff
        return fff

    print(int(rec(X)))
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

#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(X: int, Y: int):
    ans = 0
    for x in [X, Y]:
        if x == 3:
            ans += 100000
        elif x == 2:
            ans += 200000
        elif x == 1:
            ans += 300000
    if X == Y == 1:
        ans += 400000
    print(ans)
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

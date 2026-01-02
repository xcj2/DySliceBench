#!/usr/bin/env python3
import sys


def solve(N: int, X: "List[int]"):
    Y = sorted(X)
    me1 = Y[N//2]
    me2 = Y[N//2-1]

    for i in range(N):
        if X[i]<=me2:
            print(me1)
        elif X[i]>=me1:
            print(me2)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X)

if __name__ == '__main__':
    main()

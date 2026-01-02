#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, D: int, X: "List[int]", Y: "List[int]"):
    ret = 0
    for i in range(N):
        if X[i] * X[i] + Y[i] * Y[i] <= D * D:
            ret += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, D, X, Y)

if __name__ == '__main__':
    main()

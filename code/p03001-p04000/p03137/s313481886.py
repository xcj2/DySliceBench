#!/usr/bin/env python3
import sys


def solve(N: int, M: int, X: "List[int]"):
    x = sorted(X)
    x_dif = []
    for i in range(M-1):
        x_dif.append(x[i+1]-x[i])
    x_dif.sort(reverse=True)
    print(sum(x_dif[N-1:]))


    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, X)

if __name__ == '__main__':
    main()

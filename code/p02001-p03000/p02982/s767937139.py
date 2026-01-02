#!/usr/bin/env python3
import sys
import math
INF = float("inf")

tol = 1e-6


def solve(N: int, D: int, X: "List[List[int]]"):

    counter = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for a, b in zip(X[i], X[j]):
                dist += (a-b)**2
            dist = math.sqrt(dist)
            if abs(dist - round(dist)) < tol:
                counter += 1
    print(counter)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [[int(next(tokens)) for _ in range(D)]
         for _ in range(N)]  # type: "List[List[int]]"
    solve(N, D, X)


if __name__ == '__main__':
    main()

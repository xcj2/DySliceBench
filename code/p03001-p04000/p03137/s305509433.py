#!/usr/bin/env python3
import sys


def solve(N: int, M: int, X: "List[int]"):
    X.sort()
    intervals = []
    for i in range(1, M):
        intervals.append(X[i] - X[i - 1])
    intervals.sort(reverse=True)
    ret = X[-1] - X[0] - sum(intervals[:N - 1])
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, X)

if __name__ == '__main__':
    main()

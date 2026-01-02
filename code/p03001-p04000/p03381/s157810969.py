#!/usr/bin/env python3
import sys


def solve(N, X):
    Y = sorted(list(zip(X, range(N))))
    n = N // 2
    d = dict()
    for i in range(N):
        m = n - (i >= n)
        d[Y[i][1]] = Y[m][0]
    for k, v in (sorted(d.items(), key=lambda x: x[0])):
        print(v)


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

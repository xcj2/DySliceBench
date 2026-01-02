#!/usr/bin/env python3
import sys


def solve(N: int, A):
    d = [[0] * N for i in range(2)]
    d[1][N-1] = A[1][N-1]
    d[0][N-1] = A[0][N-1] + d[1][N-1]
    for i in range(2, N+1):
        d[1][N-i] = d[1][N-i+1] + A[1][N-i]
        d[0][N-i] = A[0][N-i] + max(d[1][N-i], d[0][N-i+1])
    print(d[0][0])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(2)]
    solve(N, A)

if __name__ == '__main__':
    main()

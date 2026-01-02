#!/usr/bin/env python3
import sys


def contain(N, K, A, m, i):
    for j in range(i, min(i+K, N)):
        if A[j] == m:
            return True
    return False


def solve(N, K, A):
    m = min(A)
    a = 0
    i = 0

    while i < N:
        if A[i] == m:
            i += 1
        else:
            a += 1
            i += K + contain(N, K, A, m, i) - 2
            if i < N:
                A[i] = m
    return a


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    print(solve(N, K, A))


if __name__ == '__main__':
    main()

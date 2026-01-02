#!/usr/bin/env python3
import sys


def solve(N, A):
    A = [0] + A + [0]
    C = 0
    for i in range(1, len(A)):
        C += abs(A[i] - A[i-1])
    for i in range(1, len(A)-1):
        print(C - abs(A[i] - A[i-1]) - abs(A[i] - A[i+1]) + abs(A[i-1] - A[i+1]))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()

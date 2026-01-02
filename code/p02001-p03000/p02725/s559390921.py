#!/usr/bin/env python3
import sys


def solve(K: int, N: int, A: "List[int]"):
    max = K - A[N-1] + A[0]
    for i in range(N-1):
        p = A[i+1] - A[i]
        if p > max:
            max = p
    print(K-max)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(K, N, A)

if __name__ == '__main__':
    main()

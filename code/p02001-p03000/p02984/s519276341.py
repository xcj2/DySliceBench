#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: "List[int]"):
    total = sum(A)
    x = [0]*N
    x[0] = sum([2*A[i] for i in range(0, N, 2)])-total
    for i in range(N-1):
        x[i+1] = 2*A[i]-x[i]
    print(*x, sep=" ")
    return


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

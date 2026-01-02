#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, B: "List[int]"):
    A = [0]*N
    A[0] = B[0]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    A[N-1] = B[N-2]
    print(sum(A))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve(N, B)


if __name__ == '__main__':
    main()

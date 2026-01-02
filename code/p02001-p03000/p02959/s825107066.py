#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: "List[int]", B: "List[int]"):
    count = 0
    for i in range(N):
        b = min(A[i], B[i])
        count += b
        if A[i] < B[i]:
            c = min(B[i]-A[i], A[i+1])
            count += c
            A[i+1] -= c
    print(count)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N+1)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)


if __name__ == '__main__':
    main()

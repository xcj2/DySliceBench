#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n


def solve(N: int, P: "List[int]", Q: "List[int]"):

    def rec(A):
        if len(A) == 1:
            return 1
        else:
            n = len(A)
            B = [0]*(n-1)
            for i, a in enumerate(A[1:]):
                if A[0] < a:
                    B[i] = a-1
                else:
                    B[i] = a
            return (A[0]-1)*factorial(n-1)+rec(B)

    print(abs(rec(P)-rec(Q)))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q)


if __name__ == '__main__':
    main()

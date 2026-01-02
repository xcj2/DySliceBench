#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(H: int, N: int, A: "List[int]", B: "List[int]"):
    DP = [INF]*(H+1)
    DP[0] = 0
    for i in range(H):
        for a, b in zip(A, B):
            m = min(i+a, H)
            DP[m] = min(DP[i]+b, DP[m])
    print(DP[-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(H, N, A, B)


if __name__ == '__main__':
    main()

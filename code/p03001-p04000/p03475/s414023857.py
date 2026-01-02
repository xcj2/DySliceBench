#!/usr/bin/env python3
import sys
import math


def solve(N: int, C: "List[int]", S: "List[int]", F: "List[int]"):
    for i in range(N-1): ##i駅からスタート
        t = 0
        for j in range(i,N-1):
            if t > S[j]:
                t = (S[j]+(math.ceil((t-S[j])/F[j]))*F[j]) + C[j]
            else:
                t = S[j] + C[j]
        print(t)
    print(0)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int()] * (N - 1)  # type: "List[int]"
    S = [int()] * (N - 1)  # type: "List[int]"
    F = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        C[i] = int(next(tokens))
        S[i] = int(next(tokens))
        F[i] = int(next(tokens))
    solve(N, C, S, F)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys
import numpy as np

def solve(N: int, A: "List[int]"):
    maxA = 0
    maxInd = 0
    for i in range(N):
        if A[i] > maxA:
            maxA = A[i]
            maxInd = i
    A[maxInd] = 0
    subMaxA = max(A)
    for i in range(N):
        if i == maxInd:
            A[i] = subMaxA
        else:
            A[i] = maxA
    print('\n'.join(map(str, A)))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()

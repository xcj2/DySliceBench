#!/usr/bin/env python3
import sys, math, fractions, itertools


def solve(N: int, T: "List[int]", A: "List[int]"):
    tmpT = 1
    tmpA = 1
    for i in range(N):
        d = max((tmpT-1)//T[i]+1, (tmpA-1)//A[i]+1)
        tmpT = T[i] * d
        tmpA = A[i] * d
    print(tmpT+tmpA)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]" 
    A = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        T[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, T, A)

if __name__ == '__main__':
    main()

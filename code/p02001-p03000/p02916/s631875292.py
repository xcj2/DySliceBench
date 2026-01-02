#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    r=sum(B)
    for i in range(N-1):
        if A[i+1]-A[i]==1:
            r+=C[A[i]-1]
    return r


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    print(solve(N, A, B, C))

if __name__ == '__main__':
    main()

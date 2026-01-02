#!/usr/bin/env python3
import sys


def solve(N: int, A: str, B: str, C: str):
    ret = 0
    for i in range(N):
        if A[i] == B[i] == C[i]:
            ret += 0
        elif A[i] == B[i] or B[i] == C[i] or A[i] == C[i]:
            ret += 1
        else:
            ret += 2
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = next(tokens)  # type: str
    B = next(tokens)  # type: str
    C = next(tokens)  # type: str
    solve(N, A, B, C)

if __name__ == '__main__':
    main()

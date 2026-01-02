#!/usr/bin/env python3
import sys


def solve(N: int, M: int, C: int, B: "List[int]", A: "List[List[int]]"):
    ret = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        tmp += C
        if tmp > 0:
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    B = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    A = [ [ int(next(tokens)) for _ in range(M) ] for _ in range(N) ]  # type: "List[List[int]]"
    solve(N, M, C, B, A)

if __name__ == '__main__':
    main()

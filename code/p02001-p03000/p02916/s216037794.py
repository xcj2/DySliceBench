#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    ret = 0
    for i in range(N):
        ret += B[A[i] - 1]
        if i > 0 and A[i] == A[i - 1] + 1:
            ret += C[A[i] - 2]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    B = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    C = [ int(next(tokens)) for _ in range(N-1) ]  # type: "List[int]"
    solve(N, A, B, C)

if __name__ == '__main__':
    main()

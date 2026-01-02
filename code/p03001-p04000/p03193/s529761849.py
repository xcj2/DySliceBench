#!/usr/bin/env python3
import sys


def solve(N: int, H: int, W: int, A: "List[int]", B: "List[int]"):
    answer = 0
    for i in range(N):
        if H <= A[i] and W <= B[i]:
            answer += 1
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, H, W, A, B)

if __name__ == '__main__':
    main()

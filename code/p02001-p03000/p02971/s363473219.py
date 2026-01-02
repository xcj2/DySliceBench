#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    B = sorted(A)
    max_A = B[-1]
    submax_A = B[-2]
    for i in range(N):
        if A[i] == max_A:
            print(submax_A)
        else:
            print(max_A)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()

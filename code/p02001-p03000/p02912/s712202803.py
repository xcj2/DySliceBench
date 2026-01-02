#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]"):
    while M > 0:
        A = sorted(A, reverse=True)
        MD = A[0] // 2
        for i, ai in enumerate(A):
            if ai > MD and M > 0:
                A[i] = ai//2
                M -= 1
            else:
                break
        if A[i] == 0:
            break
    print(sum(A))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()

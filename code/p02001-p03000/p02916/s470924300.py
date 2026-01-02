#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):

    result = 0
    for i, a_i in enumerate(A):
        result += B[a_i - 1]
        if i != 0:
            if a_i == (a_old + 1):
                result += C[a_i - 2]
        else:
            pass
        a_old = a_i

    print(result)

    return


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
    solve(N, A, B, C)


if __name__ == "__main__":
    main()

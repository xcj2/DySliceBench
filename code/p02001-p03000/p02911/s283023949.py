#!/usr/bin/env python3
import sys


def solve(N: int, K: int, Q: int, A: "List[int]"):

    arr = [K - Q] * N

    for a in A:
        arr[a - 1] += 1

    for go_or_not in arr:
        if go_or_not > 0:
            print("Yes")
        else:
            print("No")

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, K, Q, A)


if __name__ == "__main__":
    main()

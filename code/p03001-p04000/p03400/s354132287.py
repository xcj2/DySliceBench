#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, D: int, X: int, A: "List[int]"):
    ans = 0
    for i in range(N):
        ans += 1 + (D-1)//A[i]
    print(ans+X)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, D, X, A)


if __name__ == '__main__':
    main()

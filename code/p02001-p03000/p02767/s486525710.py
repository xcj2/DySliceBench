#!/usr/bin/env python3
import sys


def solve(N: int, X: "List[int]"):
    answer = 10**9
    for i in range(101):
        tmp = 0
        for j in range(N):
            tmp += (X[j]-i)**2
        answer = min(tmp,answer)
    print(answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X)

if __name__ == '__main__':
    main()

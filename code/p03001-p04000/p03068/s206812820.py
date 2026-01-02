#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, S: str, K: int):
    kth = S[K-1]
    s = list(S)
    for i in range(N):
        if s[i] != kth:
            s[i] = "*"
    print("".join(s))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(N, S, K)


if __name__ == '__main__':
    main()

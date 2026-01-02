#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    nww = [0] * N
    nee = [0] * N

    acc = 0
    for i in range(N - 1):
        if S[i] == "W":
            acc += 1
        nww[i + 1] = acc

    acc = 0
    for i in reversed(range(1, N)):
        if S[i] == "E":
            acc += 1
        nee[i - 1] = acc

    print(min(nwwi + neei for nwwi, neei in zip(nww, nee)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()

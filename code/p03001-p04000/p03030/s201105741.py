#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, S: "List[str]", P: "List[int]"):
    SP = []
    for i, (s, p) in enumerate(zip(S, P)):
        SP.append([i+1, s, p])
    SP.sort(key=lambda x: x[2], reverse=True)
    SP.sort(key=lambda x: x[1])
    for i, s, p in SP:
        print(i)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        P[i] = int(next(tokens))
    solve(N, S, P)


if __name__ == '__main__':
    main()

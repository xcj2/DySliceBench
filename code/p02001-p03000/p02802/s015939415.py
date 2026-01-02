#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, M: int, p: "List[int]", S: "List[str]"):
    seito = 0
    pena = 0

    AC = [False] * (N+1)
    WA = [0]*(N+1)
    for pp, ss in zip(p, S):
        if ss == "AC":
            if AC[pp] == False:
                AC[pp] = True
        else:
            if AC[pp] == False:
                WA[pp] += 1
    tot = 0
    for i in range(N+1):
        if AC[i]:
            tot += WA[i]
    print(sum(AC), tot)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int()] * (M)  # type: "List[int]"
    S = [str()] * (M)  # type: "List[str]"
    for i in range(M):
        p[i] = int(next(tokens))
        S[i] = next(tokens)
    solve(N, M, p, S)


if __name__ == '__main__':
    main()

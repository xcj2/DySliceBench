#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]", P: "List[int]"):
    sps = list(zip(S, P))
    inds = sorted(range(N), key=lambda i: (sps[i][0], -sps[i][1]))
    for i in inds:
        print(i+1)
    return


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

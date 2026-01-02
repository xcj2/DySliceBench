#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]", P: "List[int]"):
    p = []
    for i in range(N):
        p.append([S[i], -P[i], i + 1])
    #p.sort(key=lambda x: [[0])
    p.sort()
    for x in p:
        print(x[2])
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

#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]", P: "List[int]"):
    isp = [(i+1,S[i],P[i]) for i in range(N)]
    isp.sort(key= lambda x: (x[1],-x[2]))
    for t in isp:
        print(t[0])
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

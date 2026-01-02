#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, S: "List[str]", P: "List[int]"):
    sp = [[i, S[i], P[i]] for i in range(N)]

    sp = sorted(sp, key=lambda x:(x[1],-x[2]))

    for i in range(N):
        print(sp[i][0]+1)
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

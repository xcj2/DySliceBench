#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, p: "List[int]", S: "List[str]"):
    a = 0
    w = 0
    ac = [0] * (N + 1)
    wa = [0] * (N + 1)
    for i in range(M):
        if S[i] == 'WA' and not ac[p[i]]:
            wa[p[i]] += 1
        if S[i] == 'AC' and not ac[p[i]]:
            ac[p[i]] = 1
            a += 1
            w += wa[p[i]]
    print(a, w)
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

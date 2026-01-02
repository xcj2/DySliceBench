#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, S: "List[int]", C: "List[int]"):
    if N == 1:
        mn, mx = 0, 9
    if N == 2:
        mn, mx = 10, 99
    if N == 3:
        mn, mx = 100, 999
    for v in range(mn, mx + 1):
        val = str(v)
        found = True
        for i in range(M):
            if int(val[S[i] - 1]) != C[i]:
                found = False
        if found:
            print(v)
            return
    print(-1)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, s, c)

if __name__ == '__main__':
    main()

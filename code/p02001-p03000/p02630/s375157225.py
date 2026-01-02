#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]", Q: int, B: "List[int]", C: "List[int]"):
    cnts = {}
    for v in A:
        if not v in cnts:
            cnts[v] = 0
        cnts[v] += 1
    s = sum(A)
    for i in range(Q):
        b, c = B[i], C[i]
        if not b in cnts:
            cnt = 0
        else:
            cnt = cnts[b]
        s += (c - b) * cnt
        if not c in cnts:
            cnts[c] = 0
        cnts[c] += cnt
        cnts[b] = 0
        print(s)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = int(next(tokens))  # type: int
    B = [int()] * (Q)  # type: "List[int]"
    C = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, A, Q, B, C)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, S: str, l: "List[int]", r: "List[int]"):
    c = [0 for i in range(N+1)]
    for i in range(N):
        c[i+1] = c[i] + (1 if S[i:i+2] == "AC" else 0)
    for q in range(Q):
        print(c[r[q]-1] - c[l[q] - 1])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    l = [int()] * (Q)  # type: "List[int]" 
    r = [int()] * (Q)  # type: "List[int]" 
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, S, l, r)

if __name__ == '__main__':
    main()

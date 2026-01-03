#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):

    V = [[0] for _ in range(4)]
    for ww, vv in zip(w, v):
        V[ww-w[0]].append(vv)
    V = [[0]+list(accumulate(sorted(v, reverse=True))) for v in V]

    m = 0
    M = N+1
    for i in range(M):
        if i*w[0] > W:
            break
        if len(V[0]) <= i:
            break
        for j in range(M-i):
            if i*w[0] + j*(w[0]+1) > W:
                break
            if len(V[1]) <= j:
                break
            for k in range(M-i-j):
                if i*w[0] + j*(w[0]+1) + k*(w[0]+2) > W:
                    break
                if len(V[2]) <= k:
                    break
                for l in range(M-i-j-k):
                    if i*w[0] + j*(w[0]+1) + k*(w[0]+2) + l*(w[0]+3) > W:
                        break
                    if len(V[3]) <= l:
                        break
                    tot = V[0][i]+V[1][j]+V[2][k]+V[3][l]
                    m = max(m, tot)
    print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)


if __name__ == '__main__':
    main()

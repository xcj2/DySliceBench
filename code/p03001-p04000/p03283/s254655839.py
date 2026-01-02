#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, Q: int, L: "List[int]", R: "List[int]", p: "List[int]", q: "List[int]"):
    ends = {}
    for i in range(M):
        s, e = L[i], R[i]
        if not e in ends:
            ends[e] = {}
        if not s in ends[e]:
            ends[e][s] = 0
        ends[e][s] += 1

    counts = [[0]]
    for i in range(1, N + 1):
        tmp = [v for v in counts[i - 1]]
        tmp.append(0)
        if i in ends:
            for s, cnt in ends[i].items():
                tmp[s] += cnt
        counts.append(tmp)
    #print(counts)

    for s, e in zip(p, q):
        ret = 0
        for j in range(s, e + 1):
            ret += counts[e][j]
        print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]"
    q = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    solve(N, M, Q, L, R, p, q)

if __name__ == '__main__':
    main()

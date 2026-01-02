#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, X: "List[int]", L: "List[int]"):
    tmp = []
    for i in range(N):
        tmp.append((X[i] + L[i], X[i] - L[i]))
    tmp.sort()
    cur = tmp[0][1] - 1
    ret = 0
    for i in range(N):
        if cur <= tmp[i][1]:
            ret += 1
            cur = tmp[i][0]
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    L = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        L[i] = int(next(tokens))
    solve(N, X, L)

if __name__ == '__main__':
    main()

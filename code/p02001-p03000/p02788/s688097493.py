#!/usr/bin/env python3

import sys, math, bisect
sys.setrecursionlimit(300000)


def solve(N: int, D: int, A: int, X: "List[int]", H: "List[int]"):
    p = []
    for i in range(N):
        p.append([X[i], H[i]])
    p.sort()
    ret = 0
    idx = []
    val = []
    nex = 0
    minus = 0
    l = 0
    for i in range(N):
        #print(i)
        #print(p[i])
        v = ret
        while l < i and idx[l] < i:
            minus = val[l]
            l += 1
        v -= minus
        p[i][1] = max(0, p[i][1] - v * A)
        tmp = math.ceil(p[i][1] / A)
        ret += tmp
        x = p[i][0] + D
        while nex < N and p[nex][0] <= x + D:
            nex += 1
        nex -= 1
        idx.append(nex)
        val.append(ret)
        #print(idx)
        #print(val)
        #print('tmp ', tmp)
        #print(ret)
        #print()
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    H = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        H[i] = int(next(tokens))
    solve(N, D, A, X, H)

if __name__ == '__main__':
    main()

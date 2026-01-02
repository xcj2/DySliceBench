#!/usr/bin/env python3
import sys


def solve(N: int, M: int, p: "List[int]", x: "List[int]", y: "List[int]"):
    par = [i for i in range(0, N + 1)]
    def find_root(i):
        if par[i] != i:
            par[i] = find_root(par[i])
            return par[i]
        return par[i]
    def union(a, b):
        a_ = find_root(a)
        b_ = find_root(b)
        if a_ != b_:
            par[b_] = a_
        return
    for j in range(M):
        union(x[j], y[j])
    #print(par)
    ret = 0
    for i in range(N):
        val = p[i]
        idx = i + 1
        if val == idx or find_root(idx) == find_root(val):
            ret += 1
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
    p = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]" 
    y = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, p, x, y)

if __name__ == '__main__':
    main()

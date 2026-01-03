#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, x: "List[int]", y: "List[int]"):
    c = [1] * (N+1)
    p = [False] * (N+1)
    p[1] = True

    for i in range(M):
        c[y[i]] += 1
        c[x[i]] -= 1

        if p[x[i]] is True:
            p[y[i]] = True
        
        if c[x[i]] == 0:
            p[x[i]] = False

    print([i for i in p if i is True].count(True))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)

if __name__ == '__main__':
    main()

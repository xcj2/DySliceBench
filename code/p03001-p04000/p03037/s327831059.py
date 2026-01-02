#!/usr/bin/env python3
import sys


def solve(N: int, M: int, L: "List[int]", R: "List[int]"):
    l = sorted(L)
    r = sorted(R)
    ret = max(0, r[0] - l[-1] + 1)
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
    L = [int()] * (M)  # type: "List[int]" 
    R = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, L, R)

if __name__ == '__main__':
    main()

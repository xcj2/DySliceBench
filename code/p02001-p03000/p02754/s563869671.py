#!/usr/bin/env python3

import sys, math
sys.setrecursionlimit(300000)


def solve(N: int, A: int, B: int):
    tmp = math.floor(N / (A + B))
    ret = tmp * A
    ret += min(A, N - tmp * (A + B))
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)

if __name__ == '__main__':
    main()

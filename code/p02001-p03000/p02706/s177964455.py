#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, A: "List[int]"):
    s = sum(A)
    ret = N - s
    if ret < 0:
        ret = -1
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
    A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()

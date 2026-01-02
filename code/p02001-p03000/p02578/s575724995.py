#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    ret = 0
    for i in range(1, N):
        tmp = max(0, A[i - 1] - A[i])
        A[i] += tmp
        ret += tmp
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()

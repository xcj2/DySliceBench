#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, L: int):
    s = L * N + sum(list(range(N + 1))) - N
    mn = float('inf')
    ret = float('inf')
    for i in range(1, N + 1):
        t = L + i - 1
        tmp = abs(s - (s - t))
        if tmp < mn:
            ret = s - t
            mn = tmp
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, L)

if __name__ == '__main__':
    main()

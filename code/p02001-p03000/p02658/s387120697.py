#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    ret = 1
    A.sort()
    for a in A:
        ret *= a
        if ret > 10 ** 18:
            print(-1)
            return -1
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

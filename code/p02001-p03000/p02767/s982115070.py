#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, X: "List[int]"):
    ret = float('inf')
    for p in range(101):
        tmp = 0
        for u in X:
            tmp += (u - p) ** 2
        ret = min(ret, tmp)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X)

if __name__ == '__main__':
    main()

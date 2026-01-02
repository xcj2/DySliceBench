#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(X: int, N: int, p: "List[int]"):
    for i in range(1000):
        if not X - i in p:
            ret = X - i
            break
        if not X + i in p: 
            ret = X + i
            break
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(X, N, p)

if __name__ == '__main__':
    main()

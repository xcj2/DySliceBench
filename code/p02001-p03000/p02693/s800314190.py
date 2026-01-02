#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(K: int, A: int, B: int):
    ret = 'NG'
    for i in range(A, B + 1):
        if i % K == 0:
            ret = 'OK'
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(K, A, B)

if __name__ == '__main__':
    main()

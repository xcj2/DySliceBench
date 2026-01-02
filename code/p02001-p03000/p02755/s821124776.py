#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int):
    ret = -1
    for i in range(0, 10000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            ret = i
            break
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()

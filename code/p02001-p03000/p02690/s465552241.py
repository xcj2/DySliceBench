#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(X: int):
    a = 0
    b = 0
    while True:
        for x in [1, -1]:
            tmp = X + (x * b) ** 5
            if tmp < 0:
                continue
            t = int(tmp ** (1 / 5))
            if t ** 5 == tmp:
                print(t, x * b)
                return
        b += 1
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()

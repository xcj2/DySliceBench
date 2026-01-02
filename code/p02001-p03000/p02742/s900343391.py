#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(H: int, W: int):
    if H == 1 or W == 1:
        print(1)
        exit()

    if W%2 == 0:
        print(H*W//2)
    else:
        if H%2 == 0:
            print(W*(H//2))
        else:
            print(W*(H//2)+W//2+1)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(H, W)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys


def solve(H: int, W: int):
    if H == 1 or W == 1:
        print(1)
        return
        
    first = W//2 if W%2 == 0 else (W//2)+1
    second = W//2

    if H%2 == 0:
        print(first*(H//2)+second*(H//2))
    else:
        print(first*(H//2+1)+second*(H//2))
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

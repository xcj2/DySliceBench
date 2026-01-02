#!/usr/bin/env python3
import sys


def solve(H: int, W: int):
    ans = 0
    if H == 1 or W == 1:
        print(1)
        return
    elif H % 2 == 0:
        ans = (H / 2) * W
    else:
        if W % 2 == 0:
            ans = (H // 2 + 1) * W - (W // 2)
        else:
            ans = (H // 2 + 1) * W - (W // 2)
    print(int(ans))

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

#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(A: int, B: int, C: int):
    a = sorted([A, B, C])
    if a[0] == a[1] and a[1] != a[2] or a[1] == a[2] and a[1] != a[0]:
        ret = YES
    else:
        ret = NO
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
    C = int(next(tokens))  # type: int
    solve(A, B, C)

if __name__ == '__main__':
    main()

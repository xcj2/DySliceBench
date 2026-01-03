#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(A: int, B: int, C: int):
    ret = NO
    if A <= C <= B:
        ret = YES
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

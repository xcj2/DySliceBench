#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(A: int, B: int, S: str):
    ret = YES
    for i, c in enumerate(S):
        if i == A and c != '-':
            ret = NO
        if i != A and not '0' <= c <= '9':
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
    S = next(tokens)  # type: str
    solve(A, B, S)

if __name__ == '__main__':
    main()

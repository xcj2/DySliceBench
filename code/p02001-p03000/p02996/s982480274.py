#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: "List[int]", B: "List[int]"):
    tasks = sorted(zip(B, A))
    cum = 0
    for bi, ai in tasks:
        cum += ai
        if cum > bi:
            print(NO)
            return
    print(YES)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == '__main__':
    main()

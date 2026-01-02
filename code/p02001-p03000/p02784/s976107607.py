#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, N: int, A: "List[int]"):
    return H <= sum(i for i in A)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    if solve(H, N, A):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

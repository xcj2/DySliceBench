#!/usr/bin/env python3
import sys


def solve(S: int):

    if 1 <= int(S[2:]) <= 12:
        if 1 <= int(S[:2]) <= 12:
            print("AMBIGUOUS")
        else:
            print("YYMM")
    else:
        if 1 <= int(S[:2]) <= 12:
            print("MMYY")
        else:
            print("NA")

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)


if __name__ == "__main__":
    main()

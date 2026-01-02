#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(upper: str, lower: str):

    if upper == lower[::-1] and lower == upper[::-1]:
        print(YES)
    else:
        print(NO)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    upper = str(next(tokens))  # type: str
    lower = str(next(tokens))  # type: str
    solve(upper, lower)


if __name__ == '__main__':
    main()

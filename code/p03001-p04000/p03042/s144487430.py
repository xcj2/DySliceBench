#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S: str):
    mae = int(S[0:2])
    ushiro = int(S[2:])
    if 1 <= mae <= 12 and 1 <= ushiro <= 12:
        print("AMBIGUOUS")
    elif 1 <= mae <= 12:
        print("MMYY")
    elif 1 <= ushiro <= 12:
        print("YYMM")
    else:
        print("NA")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: str
    solve(S)


if __name__ == '__main__':
    main()

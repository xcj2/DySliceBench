#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("yes")  # type: str


def no():
    print("no")  # type: str


def solve(S: str):
    S = list(S)
    S.sort()
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            no()
            return
    yes()
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()

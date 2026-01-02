#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def kaibun(s):
    return s == s[::-1]


def solve(S: str):
    N = len(S)

    if not kaibun(S):
        no()
        return

    s = S[:(N-1)//2]
    # print(s)
    if not kaibun(s):
        no()
        return

    s = S[(N+1)//2:]
    # print(s)
    if not kaibun(s):
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

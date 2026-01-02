#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str):
    N = len(S)
    for i in range(N // 2):
        if S[i] != S[N - i - 1]:
            print(NO)
            return NO
    m = N // 2
    for i in range(m // 2):
        if S[i] != S[m - i - 1]:
            print(NO)
            return NO

    print(YES)
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

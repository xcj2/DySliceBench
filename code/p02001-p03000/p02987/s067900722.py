#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str):
    isGood = False
    if S[0] == S[1]:
        if S[2] == S[3] and S[0] != S[2]:
            isGood = True
    elif S[0] == S[2]:
        if S[1] == S[3] and S[0] != S[1]:
            isGood = True
    elif S[0] == S[3] and S[0] != S[1]:
        if S[1] == S[2]:
            isGood = True
    else:
        isGood = False
    if isGood:
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
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()

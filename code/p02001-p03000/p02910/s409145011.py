#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str
odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']

def solve(S: str):
    for i in range(len(S)):
        if i % 2 == 0:
            if not S[i] in odd:
                print(NO)
                sys.exit(0)
        else:
            if not S[i] in even:
                print(NO)
                sys.exit(0)
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

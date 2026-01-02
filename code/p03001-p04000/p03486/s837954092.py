#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(s: str, t: str):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort(reverse= True)
    s = ''.join(s)
    t = ''.join(t)
    if s<t:
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
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)

if __name__ == '__main__':
    main()

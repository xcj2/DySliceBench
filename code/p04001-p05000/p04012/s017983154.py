#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(w: str):
    count = [0] * 26
    for c in w:
        count[ord(c) - ord('a')] += 1
    for cnt in count:
        if cnt % 2:
            print(NO)
            return
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    w = next(tokens)  # type: str
    solve(w)

if __name__ == '__main__':
    main()

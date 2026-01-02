#!/usr/bin/env python3
import sys


def solve(S: str):
    max_len = 0
    def isvalid(s):
        return s in ['A', 'C', 'G', 'T']

    for i in range(len(S)):
        if not isvalid(S[i]):
            continue
        j = i + 1
        while j < len(S) and isvalid(S[j]):
            j += 1
        max_len = j-i if j-i > max_len else max_len
    print(max_len)
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

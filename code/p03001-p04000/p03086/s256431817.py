#!/usr/bin/env python3
import sys


def solve(S: str):
    def is_valid(s):
        for c in s:
            if not c in 'AGTC':
                return False
        return True
    n = len(S)
    ret = ''
    for i in range(n):
        for j in range(i, n):
            if is_valid(S[i:j + 1]) and j - i + 1 > len(ret):
                ret = S[i:j + 1]
    print(len(ret))
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

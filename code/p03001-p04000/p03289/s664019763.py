#!/usr/bin/env python3
import sys


def solve(S: str):
    ret = 'AC'
    if S[0] != 'A':
        ret = 'WA'
    else:
        count = 0
        for i, c in enumerate(S[1:]):
            if not c.islower():
                if count < 1 and c == 'C' and i >= 1 and i <= len(S) - 3:
                    count += 1
                else:
                    ret = 'WA'
                    break
        if count < 1:
            ret = 'WA'
    print(ret)
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

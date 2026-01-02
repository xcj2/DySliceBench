#!/usr/bin/env python3
import sys

def is_m(n):
    if n > 0 and n < 13:
        return True
    return False


def solve(S: str):
    a = int(S[:2])
    b = int(S[2:])
    if is_m(a) and not is_m(b):
        ret = 'MMYY'
    elif not is_m(a) and is_m(b):
        ret = 'YYMM'
    elif is_m(a) and is_m(b):
        ret = 'AMBIGUOUS'
    else:
        ret = 'NA'
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()

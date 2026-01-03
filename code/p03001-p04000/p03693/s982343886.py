#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(r: int, g: int, b: int):
    if (r * 100 + g * 10 + b) % 4 == 0:
        ret = YES
    else:
        ret = NO
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = int(next(tokens))  # type: int
    g = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(r, g, b)

if __name__ == '__main__':
    main()

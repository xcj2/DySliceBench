#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(x: int, y: int):
    g = [4, 6, 9, 11]
    ret = YES
    if x == 2 or y == 2:
        ret = NO
    elif x in g and not y in g or y in g and not x in g:
        ret = NO
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)

if __name__ == '__main__':
    main()

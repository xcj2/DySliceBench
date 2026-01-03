#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(a: int, b: int, c: int):
    ret = NO
    s = a + b + c
    if s % 2 == 0 and (a == s // 2 or b == s // 2 or c == s // 2):
        ret = YES
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    solve(a, b, c)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys


def solve(A: int, B: int):
    def is_pal(n):
        s = str(n)
        for i in range(len(s)):
            if s[i] != s[-1 - i]:
                return False
        return True
    ret = 0
    for i in range(A, B + 1):
        if is_pal(i):
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()

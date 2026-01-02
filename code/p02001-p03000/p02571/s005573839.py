#!/usr/bin/env python3

import sys

DEBUG = False


def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep=" "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    s = read(str)
    t = read(str)

    min_mismatch = 10000
    for start in range(0, len(s) - len(t) + 1):
        mismatch = 0
        for i in range(start, start + len(t)):
            if s[i] != t[i - start]:
                mismatch += 1
        if mismatch < min_mismatch:
            min_mismatch = mismatch
    print(min_mismatch)


if __name__ == "__main__":
    main()

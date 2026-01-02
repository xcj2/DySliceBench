#!/usr/bin/env python3

import sys

DEBUG = False

def solve():
    return


def read_int_list(sep = " "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]

def read_int():
    return int(sys.stdin.readline())

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    _, x = read_int_list()
    ls = read_int_list()

    ans = 1
    p = 0
    for l in ls:
        if p + l > x:
            break
        p += l
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
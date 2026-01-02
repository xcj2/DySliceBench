#!/usr/bin/env python3

import sys

DEBUG = False

def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep = " "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    n, m = read_list(int)
    as_ = read_list(int)
    all_voting = sum(as_)
    if len(list(filter(lambda v: v >= all_voting / (4 * m), as_))) >= m:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
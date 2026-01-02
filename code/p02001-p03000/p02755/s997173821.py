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
    a, b = read_int_list()
    for i in range(0, 1250):
        if int(i * 0.08) != a:
            continue
        if int(i * 0.1) != b:
            continue
        print(i)
        return
    print(-1)



if __name__ == "__main__":
    main()
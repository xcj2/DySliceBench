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
    n, blue, red = read_int_list()
    ans = 0
    nr_cycle = n // (blue + red)
    ans += nr_cycle * blue
    n = n % (blue + red)
    if blue < n:
        ans += blue
    else:
        ans += n
    print(ans)

if __name__ == "__main__":
    main()
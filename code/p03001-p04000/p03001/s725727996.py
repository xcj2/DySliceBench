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
    w, h, x, y = read_int_list()
    nr_ans = 1
    center_point = (h / 2, w / 2)
    if abs(center_point[0] - y) < 1e-9 and abs(center_point[1] - x) < 1e-9:
        nr_ans = 2
    print("%f %d" % (w * h / 2, nr_ans - 1))


if __name__ == "__main__":
    main()
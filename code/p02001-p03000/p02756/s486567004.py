#!/usr/bin/env python3

import sys
from collections import deque

DEBUG = False

def solve():
    return


def read_int_list(sep = " "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]

def read_int():
    return int(sys.stdin.readline())

def read_str():
    return sys.stdin.readline().rstrip()
    
def read_str_list(sep = " "):
    return [s for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    d = deque(list(read_str()))
    q = read_int()

    reversed_ = False
    for _ in range(0, q):
        query = read_str_list()
        if query[0] == "1":
            reversed_ = not reversed_
            continue
        # query[0] == "2"
        f, c = query[1:]
        if (f == "1" and not reversed_) or (f == "2" and reversed_):  # insert to the left
            d.appendleft(c)
        else:
            d.append(c)
    if reversed_:
        print("".join(reversed(list(d))))
    else:
        print("".join(list(d)))


if __name__ == "__main__":
    main()
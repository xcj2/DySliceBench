#!/usr/bin/env python3

import sys
from collections import namedtuple

Query = namedtuple("Query", ("s", "c"))

DEBUG = False


def read_int_list(sep = " "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]

def read_int():
    return int(sys.stdin.readline())

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def checkq(n, num, queries):
    digits = []
    if num == 0:
        digits = [0]
    while num > 0:
        digits.append(num % 10)
        num //= 10
    if len(digits) != n:
        return False
    for q in queries:
        if digits[-q.s] != q.c:
            return False
    return True


def main():
    n, m = read_int_list()
    queries = []
    for _ in range(0, m):
        queries.append(Query(*read_int_list()))
    for i in range(0, 1000):
        if checkq(n, i, queries):
            print(i)
            return
    print(-1)


if __name__ == "__main__":
    main()
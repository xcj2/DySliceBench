#!/usr/bin/env python3

import sys
from collections import namedtuple

DEBUG = False

def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep = " "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return

Item = namedtuple("Item", ("value", "weight"))

def main():
    n, max_w = read_list(int)
    items = []

    for _ in range(n):
        v, w = read_list(int)
        items.append(Item(v, w))
    
    dp = [0] * (max_w + 1)
    for w_i in range(max_w + 1):
        for i in range(len(items)):
            if w_i >= items[i].weight:
                dp[w_i] = max(dp[w_i], dp[w_i - items[i].weight] + items[i].value)
    print(dp[max_w])

if __name__ == "__main__":
    main()


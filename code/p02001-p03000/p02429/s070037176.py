#!/usr/bin/env python3
# ITP2_11_C: Bitset 2 - Enumeration of Subsets 3

from functools import lru_cache


def subset(n, mask):
    @lru_cache(maxsize=None)
    def _subset(i):
        if i < 0:
            return [(0, [])]
        m = mask[i]
        return (_subset(i-1) +
                [(v + (1 << m), vs + [m]) for v, vs in _subset(i-1)])

    return _subset(len(mask)-1)


def run():
    n = int(input())
    mask = tuple([int(i) for i in input().split()][1:])

    for i, vs in subset(n, mask):
        print("{}:{}".format(i, "".join([" {}".format(v) for v in vs])))


if __name__ == '__main__':
    run()


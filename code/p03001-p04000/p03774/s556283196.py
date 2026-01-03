#!/usr/bin/env python3

import collections


Point = collections.namedtuple("Point", "x y idx")


def manhattan_dist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def find_res_point(st, ps):
    def key(p):
        return (manhattan_dist(st, p), p.idx)
    return min(ps, key=key)


def solve(sts, ps):
    return (find_res_point(st, ps) for st in sts)


def main():
    n, m = (int(x) for x in input().split())
    sts = []
    for i in range(n):
        a, b = (int(x) for x in input().split())
        sts.append(Point(a, b, i + 1))
    ps = []
    for j in range(m):
        c, d = (int(x) for x in input().split())
        ps.append(Point(c, d, j + 1))
    for p in solve(sts, ps):
        print(p.idx)


if __name__ == '__main__':
    main()

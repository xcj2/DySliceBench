# https://atcoder.jp/contests/abc113/tasks/abc113_c

import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, m = input_int_list()
    cnt = defaultdict(int)
    cities = []
    ids = [None] * m
    for i in range(0, m):
        p, y = input_int_list()
        cities.append((i, p, y))

    cities = sorted(cities, key=lambda x: x[2])

    for i, p, y in cities:
        num = cnt[p] + 1
        cnt[p] += 1
        _id = "{:0=6}{:0=6}".format(p, num)
        ids[i] = _id

    for _id in ids:
        print(_id)

    return


if __name__ == "__main__":
    main()

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

def nr_choose2(nr_ball):
    return nr_ball * (nr_ball - 1) // 2

def main():
    n = read(int)
    as_ = read_list(int)
    nr_balls_by_num = {}
    nr_choose2_by_num = {}
    for a in as_:
        if a not in nr_balls_by_num:
            nr_balls_by_num[a] = 0
        nr_balls_by_num[a] += 1

    nr_all_choose2 = 0
    for num in nr_balls_by_num:
        nr_choose2_by_num[num] = nr_choose2(nr_balls_by_num[num])
        nr_all_choose2 += nr_choose2_by_num[num]

    for k in range(len(as_)):
        ans = nr_all_choose2 - nr_choose2_by_num[as_[k]]
        ans += nr_choose2(nr_balls_by_num[as_[k]] - 1)
        print(ans)


if __name__ == "__main__":
    main()
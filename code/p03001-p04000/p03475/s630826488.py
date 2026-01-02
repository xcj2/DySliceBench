#!/usr/bin/env python3

import functools


def div_ceil(a, b):
    return (a + b - 1) // b


def simulate(cs, ss, fs, goal_sta, start_sta):
    assert start_sta <= goal_sta
    cur_t = 0
    for i in range(start_sta, goal_sta):
        next_start_t = max(ss[i], div_ceil(cur_t, fs[i]) * fs[i])
        cur_t = next_start_t + cs[i]
    return cur_t


def solve(n, cs, ss, fs):
    sim_from = functools.partial(simulate,
                                 cs=cs, ss=ss, fs=fs, goal_sta=n - 1)
    return [sim_from(start_sta=i) for i in range(n)]


def main():
    n = int(input())
    cs = [-1 for _ in range(n - 1)]
    ss = [-1 for _ in range(n - 1)]
    fs = [-1 for _ in range(n - 1)]
    for i in range(n - 1):
        cs[i], ss[i], fs[i] = (int(z) for z in input().split())
    print(*solve(n, cs, ss, fs), sep="\n")


if __name__ == '__main__':
    main()

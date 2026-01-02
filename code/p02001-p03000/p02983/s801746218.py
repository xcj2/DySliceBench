#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    l, r = MI()

    if r - l >= 2018:
        print(0)
        return

    mod_l = l % 2019
    mod_r = r % 2019

    candidates = []

    if mod_l < mod_r:
        candidates.extend(range(mod_l, mod_r + 1))
    else:
        candidates.extend(range(0, mod_r + 1))
        candidates.extend(range(mod_l, 2019))
    min_ans = 2019

    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            tmp = (candidates[i] * candidates[j]) % 2019
            if tmp < min_ans:
                min_ans = tmp

    print(min_ans)


main()

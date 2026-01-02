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
    h, w, m = MI()
    targets = [[] for i in range(h)]
    tate = [[] for i in range(w)]
    tate_length = [0] * w
    original = []
    lengths = [0] * h
    for i in range(m):
        target = LI()
        original.append(target)
        targets[target[0] - 1].append(target[1] - 1)
        tate[target[1] - 1].append(target[0] - 1)
        lengths[target[0] - 1] += 1
        tate_length[target[1] - 1] += 1

    max_length = max(lengths)
    max_length_tate = max(tate_length)

    max_w_indexes = [i for i, x in enumerate(
        tate_length) if x == max_length_tate]

    max_h_indexes = [i for i, x in enumerate(
        lengths) if x == max_length]

    max_h_indexes = set(max_h_indexes)
    max_w_indexes = set(max_w_indexes)

    ttl = len(max_h_indexes) * len(max_w_indexes)

    for target in original:
        if target[0] - 1 in max_h_indexes and target[1] - 1 in max_w_indexes:
            ttl -= 1

    if ttl > 0:
        print(max_length + max_length_tate)
    else:
        print(max_length+max_length_tate - 1)


main()

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
    N = II()
    targets = LI()
    MAX_INT = max(targets) + 1
    counter = cl.Counter(targets)
    targets = set(targets)
    is_pw = True

    num_1 = counter[1]
    if num_1 > 1:
        N -= num_1 - 1

    if len(targets) != N:
        is_pw = False

    if len(targets) == 1:
        if 1 in targets:
            print("pairwise coprime")
            return
        print("not coprime")
        return

    for i in range(2, MAX_INT):
        origin = i
        kosuu = 0
        while origin <= MAX_INT:
            if origin in targets:
                kosuu += 1
            origin += i

        if kosuu <= 1:
            continue
        elif kosuu < len(targets):
            is_pw = False
        else:
            print("not coprime")
            return

    if is_pw:
        print("pairwise coprime")
        return
    print("setwise coprime")


main()

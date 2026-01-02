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
    n = II()
    t = input()
    conter = cl.Counter(t)
    num_w = conter["W"]
    num_r = conter["R"]
    w_in_r = 0
    r_in_r = 0
    for i in range(num_r):
        if t[i] == "W":
            w_in_r += 1
        else:
            r_in_r += 1
    r_in_w = num_r - r_in_r
    print(max(w_in_r, r_in_w))


main()

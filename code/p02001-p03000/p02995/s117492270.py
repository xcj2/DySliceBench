#!/usr/bin/env python3
import collections as cl
import math
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def find_target(x, c, d):
    num_c = x // c
    num_d = x // d
    lcm_cd = lcm(c, d)
    num_dip = x // lcm_cd
    return x - (num_c + num_d - num_dip)


def main():
    a, b, c, d = MI()
    target_in_a = find_target(a - 1, c, d)
    target_in_b = find_target(b, c, d)
    print(target_in_b - target_in_a)


main()

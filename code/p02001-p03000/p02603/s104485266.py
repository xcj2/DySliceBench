#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def std_in():
    return sys.stdin.readline().strip()


def main():
    n = int(std_in())
    a = list(get_ints())
    a.append(0)
    m = 1000
    k = 0

    for i in range(n):
        if i == n:
            break
        if a[i] > a[i+1]:
            m += k * a[i]
            k = 0
        elif a[i] < a[i+1]:
            q, mod = divmod(m, a[i])
            k += q
            m = mod
    print(m)


if __name__ == "__main__":
    main()

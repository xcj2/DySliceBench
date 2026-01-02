#!/usr/bin/env python3


def next_line():
    return input()


def next_int():
    return int(input())


def int_ar():
    return list(map(int, input().split()))


def strs():
    return input().split()


def ints():
    return map(int, input().split())


def int_ar_mul(size):
    return [int(input()) for _ in range(size)]


def str_ar(size):
    return [input() for _ in range(size)]


def main():
    n, k = ints()
    p = sorted(int_ar())
    res = 0
    for i in range(k):
        res += p[i]
    print(res)


if __name__ == '__main__':
    main()

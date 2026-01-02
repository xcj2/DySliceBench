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

    kabu_price = LI()

    cash = 1000
    kabu = 0

    for i in range(N - 1):
        ratio = kabu_price[i + 1] / kabu_price[i]

        if ratio == 1:
            continue

        if ratio < 1:
            if kabu > 0:
                cash += kabu * kabu_price[i]
                kabu = 0

        if ratio > 1:
            if cash >= kabu_price[i]:
                num_parcha = cash // kabu_price[i]
                kabu += num_parcha
                cash = cash % kabu_price[i]

    cash += kabu * kabu_price[-1]

    print(cash)


main()

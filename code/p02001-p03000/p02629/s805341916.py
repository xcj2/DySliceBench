#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()

def Base_10_to_n(i10, n, ans_list:list):
    # 各桁を0-indexにするために1減らす
    i10 -= 1
    if(int(i10/n)):
        ans_list.append(Base_10_to_n(int(i10/n), n, ans_list))
        return str(i10%n)
    return str(i10%n)


def resolve():
    n = int(input().rstrip())
    n_list = []
    ans_list = []

    n_list.append(Base_10_to_n(n, 26, n_list))

    for n26 in n_list:
        string = ord("a") + int(n26)
        ans_list.append(chr(string))

    ans_string = ""
    for st in ans_list:
        ans_string += st
    print(ans_string.rstrip())

if __name__ == "__main__":
    resolve()


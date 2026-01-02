#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix

DICT_SIZE = 1000003
REHASH = 10007
DICT = [None] * DICT_SIZE


def hash_value(S):
    M = 257
    val = 0
    for c in S:
        val = (val * M + ord(c)) % DICT_SIZE
    return val


def insert(s):
    h = hash_value(s)
    while DICT[h] is not None:
        if DICT[h] == s:
            return
        h = (h + REHASH) % DICT_SIZE
    DICT[h] = s


def find(s):
    h = hash_value(s)
    while True:
        if DICT[h] is None:
            return 'no'
        elif DICT[h] == s:
            return 'yes'
        h = (h + REHASH) % DICT_SIZE


if __name__ == "__main__":

    n = int(input())

    for _ in range(n):
        cmd, s = input().split()
        if cmd == 'insert':
            insert(s)
        else:
            print(find(s))


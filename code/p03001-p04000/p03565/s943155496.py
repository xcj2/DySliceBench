#!/usr/bin/env python3
import sys


input = sys.stdin.readline
def IS(cb): return cb(input().strip())
def IL(cb): return [cb(s) for s in input().strip().split()]
def IR(cb, rows): return [IS(cb) for _ in range(rows)]
def ILL(cb, rows): return [IL(cb) for _ in range(rows)]


def solve():
    Sd = IS(str)
    T = IS(str)
    T_len = len(T)

    for i in range(len(Sd) - T_len, -1, -1):
        S_i = Sd[i: i + T_len]
        matched = all([s == '?' or s == t for s, t in zip(S_i, T)])
        if matched:
            left = ''.join(['a' if s == '?' else s for s in Sd[: i]])
            right = ''.join(['a' if s == '?' else s for s in Sd[i + T_len:]])
            print(left + T + right)
            exit()
    print('UNRESTORABLE')

solve()

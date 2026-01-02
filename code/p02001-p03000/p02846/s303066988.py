#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()

def srl(proc=None):
    if proc is not None:
        return list(map(proc, rl().split()))
    else:
        return rl().split()

def main():
    t1, t2 = srl(int)
    a1, a2 = srl(int)
    b1, b2 = srl(int)
    if a1 < b1:
        a1, b1 = b1, a1
        a2, b2 = b2, a2
    if a1 * t1 + a2 * t2 == b1 * t1 + b2 * t2:
        print('infinity')
        return
    elif a1 * t1 + a2 * t2 > b1 * t1 + b2 * t2:
        print('0')
        return
    s1 = a1*t1 - b1*t1
    s2 = a1 * t1 + a2 * t2 - b1 * t1 - b2 * t2
    s2 = -s2
    b = int(s1 % s2 == 0)
    k = s1 // s2 + 1
    print(2*k-1-b)

if __name__ == '__main__':
    main()

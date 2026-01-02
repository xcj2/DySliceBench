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
    N = rl(int)
    a = []
    for _ in range(N):
        s, t = srl()
        t = int(t)
        a.append((s, t))
    q = rl()
    ret = sum(x[1] for x in a)
    for s, t in a:
        ret -= t
        if s == q:
            break
    print(ret)

if __name__ == '__main__':
    main()

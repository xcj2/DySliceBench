import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import collections as cl
import functools as ft
import numpy as np

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def count_lr_old(n, m, a):
    count = 0
    for l in range(n):
        for r in range(l, n):
            if not sum(a[l:r+1]) % m:
                count += 1
    return count


def count_lr(n, m, a):
    b_acm = 0
    mod_m_counts = {}
    for ai in a:
        b_acm = (b_acm + ai) % m
        mod_m_counts.setdefault(b_acm, 0)
        mod_m_counts[b_acm] += 1

    # print(mod_m_counts)

    # print('len a:', len(a))
    count = 0
    all_ = 0
    for k, v in mod_m_counts.items():
        all_ += v
        count += v * (v - 1) // 2
        if k == 0:
            count += v

    # print('all_', all_)
    return count


if __name__ == "__main__":
    n, m = LI()
    a = LI()

    print(count_lr(n, m, a))

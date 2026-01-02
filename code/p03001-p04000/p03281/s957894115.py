import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import operator as op
import collections as cl
import functools as ft

def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))
def LF(): return list(map(float, input().split()))
def LS(): return input().split()
def I(): return int(input())
def F(): return float(input())
def S(): return input()


def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def divisorize(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]


def count_divisor(fct):
    counts_plus1 = [count+1 for _, count in fct]
    total = ft.reduce(op.mul, counts_plus1)

    return total


if __name__ == '__main__':
    n = I()
    count_8 = 0
    for i in range(3, n+1, 2):
        fct = factorize(i)
        if count_divisor(fct) == 8:
            count_8 += 1

    print(count_8)

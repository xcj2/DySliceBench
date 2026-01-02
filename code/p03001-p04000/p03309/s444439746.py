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


def calc_lament(a, b):
    return sum([abs(ai - b) for ai in a])


n = int(input())
a = LI()

a = [ai - i for ai, i in zip(a, range(1, n+1))]

b = int(np.median(a))
print(calc_lament(a, b))

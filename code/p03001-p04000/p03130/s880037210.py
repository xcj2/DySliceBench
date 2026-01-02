import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools


sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    a1, b1 = LI()
    a2, b2 = LI()
    a3, b3 = LI()

    l = [0, 0, 0, 0]
    l[a1-1] += 1
    l[a2-1] += 1
    l[a3-1] += 1
    l[b1-1] += 1
    l[b2-1] += 1
    l[b3-1] += 1

    return max(l) <= 2


if main():
    print('YES')
else:
    print('NO')


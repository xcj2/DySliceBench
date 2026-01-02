import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from bisect import bisect_left
from itertools import accumulate


n = ni()
a = list(li())

suma = sum(a)
cuma = [0] + list(accumulate(a))
half = suma / 2
halfidx = bisect_left(cuma, half) - 1
if halfidx == -1:
    print(cuma[1] - (cuma[n] - cuma[1]))
else:
    first = cuma[n] - cuma[halfidx] - cuma[halfidx]
    latter = cuma[halfidx+1] - (cuma[n] - cuma[halfidx+1])
    print(min(first, latter))



import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

from itertools import accumulate
from bisect import bisect_left

x = ni()
jump = [i for i in range(1,10**5)]
jump_cum = list(accumulate(jump))
print(bisect_left(jump_cum, x) + 1)
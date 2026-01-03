import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from bisect import bisect_left
from itertools import accumulate

n = ni()
oneton = [i for i in range(10**4)]
acc = list(accumulate(oneton))

maxp = bisect_left(acc, n)
for p in range(1,maxp+1):
    if p == acc[maxp] - n:
        continue
    print(p)
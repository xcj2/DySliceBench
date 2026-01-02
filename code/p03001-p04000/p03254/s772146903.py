import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate
from bisect import bisect_right

n,x = li()
a = list(li())

a.sort()
a_cum = list(accumulate(a))


if x == a_cum[-1]:
    print(n)

elif x > a_cum[-1]:
    print(n-1)
    
else:
    ans = bisect_right(a_cum, x)
    print(ans)
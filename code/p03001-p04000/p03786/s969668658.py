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

n = ni()
a = li()

a.sort()
a_cum = list(accumulate(a))[::-1]
a.sort(reverse=True)

ans = n

for i in range(n-1):
    if a[i] <= 2*a_cum[i+1]:
        continue
    else:
        ans = i+1
        break
        
print(ans)
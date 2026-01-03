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

n,k = li()
a = li()

a_cum = list(accumulate([0] + a))
a_pl = [ai if ai>0 else 0 for ai in a]
a_left = list(accumulate([0] + a_pl))
a_right = list(accumulate([0] + a_pl[::-1]))

ans = 0

for i in range(n-k+1):
    # a[i:i+k]を黒にするとき
    cand = a_cum[i+k] - a_cum[i]
    cand += (a_left[i] + a_right[n-(i+k)])
    ans = max(ans,cand)
    
    
    # a[i:i+k]を白にするとき
    cand = 0
    cand += (a_left[i] + a_right[n-(i+k)])
    ans = max(ans,cand)
    
    
print(ans)
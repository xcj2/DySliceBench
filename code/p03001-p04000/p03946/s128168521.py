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

from collections import Counter

n,t = li()
a = li()

a_rev = a[::-1]
itv_max_rev = [0]
for i in range(n-1):
    itv_max_rev.append(max(itv_max_rev[-1], a_rev[i]))
    
itv_max = itv_max_rev[::-1]

cnt = Counter([])
for ai,ivmi in zip(a, itv_max):
    cnt[ivmi - ai] += 1
    
max_key = max(cnt.keys())
print(cnt[max_key])
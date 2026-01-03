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

cnt = Counter([])

n,k = li()

num = []
index = []

for _ in range(n):
    a,b = li()
    cnt[a] += b


res = k
for key in sorted(cnt.keys()):
    if res - cnt[key] <= 0:
        print (key)
        break
    
    res -= cnt[key]
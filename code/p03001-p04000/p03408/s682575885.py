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

from collections import Counter

n = ni()
blue = []
for _ in range(n):
    blue.append(ns())
    
m = ni()
red = []
for _ in range(m):
    red.append(ns())
    
blc = Counter(blue)
rdc = Counter(red)

ans = 0
for bk, bv in blc.items():
    if bk in rdc.keys():
        ans = max(ans, bv - rdc[bk])
    else:
        ans = max(ans, bv)
        
        
print(ans)

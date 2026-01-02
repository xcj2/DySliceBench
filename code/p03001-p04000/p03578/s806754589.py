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
d = list(li())

m = ni()
t = list(li())

dcnt = Counter(d)
tcnt = Counter(t)

exist = True

for tkey, tval in tcnt.items():
    if tval > dcnt[tkey]:
        exist = False
        
print("YES" if exist else "NO")
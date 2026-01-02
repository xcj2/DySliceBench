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

from heapq import heappush, heappop
from collections import defaultdict

x,y,z,k = li()
a = list(li())
b = list(li())
c = list(li())

a.sort()
b.sort()
c.sort()

acur = x-1
bcur = y-1
ccur = z-1

deli = []
que = [(-a[-1]-b[-1]-c[-1], x-1, y-1, z-1)]
searched = defaultdict(bool)

while len(deli) < k:
    good, acur, bcur, ccur = heappop(que)
    deli.append(-good)
    
    if acur > 0 and not searched[(acur-1, bcur, ccur)]:
        heappush(que, (-a[acur-1]-b[bcur]-c[ccur], acur-1, bcur, ccur))
        searched[(acur-1, bcur, ccur)] = True
    
    if bcur > 0 and not searched[(acur, bcur-1, ccur)]:
        heappush(que, (-a[acur]-b[bcur-1]-c[ccur], acur, bcur-1, ccur))
        searched[(acur, bcur-1, ccur)] = True
    
    if ccur > 0 and not searched[(acur, bcur, ccur-1)]:
        heappush(que, (-a[acur]-b[bcur]-c[ccur-1], acur, bcur, ccur-1))
        searched[(acur, bcur, ccur-1)] = True
        
for di in deli:
    print(di)
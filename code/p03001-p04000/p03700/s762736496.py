from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,a,b = inpl()
h = [inp() for _ in range(n)]
ok = 10**12
ng = 0
c = a-b
def chk(x):
    cnt = 0
    for t in h:
        t -= b*x
        if t <= 0: continue
        cnt += (t+c-1)//c
    if cnt <= x:
        return True
    return False
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if chk(mid):
        ok = mid
    else:
        ng = mid
print(ok)
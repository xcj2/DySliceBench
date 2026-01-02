from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


n,k = inpl()
a = inpl()
ok = max(a)
ng = 0
def sol(x):
    cnt = 0
    for i in range(n):
        cnt += (a[i]+x-1)//x-1
    if cnt <= k:
        return True
    return False
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if sol(mid):
        ok = mid
    else:
        ng = mid
print(ok)
from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
a = inpl(); a.sort()
ok = a[0] + a[0] - 1
ng = a[-1] + a[-1] + 1
def sol(x):
    res = 0
    for i in range(n):
        y = x-a[i]
        res += n-bisect_left(a,y)
    return True if res >= m else False
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if sol(mid):
        ok = mid
    else:
        ng = mid
b = [0]
for i in range(n)[::-1]:
    b.append(b[-1]+a[i])
res = 0
cnt = 0
# print(b,ok)
for x in a:
    ind = n-bisect_left(a,ok-x)
    cnt += ind
    res += b[ind] + x*ind
print(res-(cnt-m)*ok)

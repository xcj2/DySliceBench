from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
a = sorted(inpl())
ng = 10**9+1
ok = -1
def sol(x):
    cnt = 0
    for i,t in enumerate(a):
        tmp = x - t
        c = bisect.bisect_left(a,tmp)
        cnt += n-c
    return True if cnt >= m else False

while ng-ok > 1:
    mid = (ng+ok)//2
    if sol(mid):
        ok = mid
    else: ng = mid
    # print(ok,ng)
# print(ok)
res = 0
cnt = 0
revc = [0]
for i in range(n)[::-1]:
    revc.append(revc[-1] + a[i])
# print(revc)
for i in range(n):
    j = n-bisect.bisect_left(a,ok-a[i])
    res += j*a[i] + revc[j]
    cnt += j
res -= (cnt-m) * ok
print(res)
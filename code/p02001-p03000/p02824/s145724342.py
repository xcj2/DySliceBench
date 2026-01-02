from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,m,v,p = inpl()
a = inpl()
c = Counter(a)
a.sort()
b_num = a[n-p]
d_cnt = 0
b_cnt = 0
u_cnt = 0
for i in a:
    if i < b_num: d_cnt += 1
    elif i == b_num: b_cnt += 1
    else: u_cnt += 1

def f(x,i):
    if x >= b_num:
        return True
    if x + m < b_num:
        return False
    if i + 1 + u_cnt >= v:
        return True
    cnt = 0
    for item in a:
        if item > b_num or item <= x:
            cnt += m
        else:
            cnt += x + m - item
    # print(cnt)
    if cnt >= m*v:
        return True
    else:
        return False
# print(f(a[2],2))
ok = n-1
ng = -1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if f(a[mid],mid):
        ok = mid
    else:
        ng = mid
print(n-ok)

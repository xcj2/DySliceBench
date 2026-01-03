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

n = inp()
a = inpl()
u = False
d = False
res = 1
i = 0
while i < n-1:
    if u and a[i+1] < a[i]:
        res += 1
        u = False
        i += 1
    elif d and a[i+1] > a[i]:
        res += 1
        d = False
        i += 1
    if i < n-1:
        if a[i+1] > a[i]:
            u = True
        elif a[i+1] < a[i]:
            d = True
    i += 1
print(res)
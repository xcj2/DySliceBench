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
s = sum(a)
cnt = 0
res = INF
b = [0] * n
for i in range(n-1):
    a[i+1] = a[i+1] + a[i]
for i in range(n):
    res = min(res,abs(s-a[i]-a[i]))
print(res)
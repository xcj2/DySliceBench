from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
s = [input() for i in range(n)]
m = inp()
t = [input() for i in range(m)]
ds = defaultdict(int)
dt = defaultdict(int)
for i in s:
    ds[i] += 1
for i in t:
    dt[i] += 1
res = 0
for key in ds.keys():
    res = max(res, ds[key] - dt[key])
print(res)

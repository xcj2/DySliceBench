from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a,b = inpl()
p = inpl()
d = defaultdict(int)
for i in p:
    if i <= a:
        d[0] += 1
    elif a < i <= b:
        d[1] += 1
    else:
        d[2] += 1
print(min(d[0],d[1],d[2]))
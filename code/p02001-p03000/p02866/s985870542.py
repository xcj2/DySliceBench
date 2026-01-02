from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
d = defaultdict(int)
m = 0
for i in a:
    d[i] += 1
    m = max(m,i)
res = 1
tmp = 1
for i in range(m+1):
    if i == 0:
        if d[i] != 1 or a[0] != 0:
            print(0)
            quit()
        continue
    if d[i] == 0:
        res = 0
        break
    if i == 1:
        tmp = d[i]
        continue
    res *= (tmp ** d[i] )%998244353
    tmp = d[i]
print(res%998244353)

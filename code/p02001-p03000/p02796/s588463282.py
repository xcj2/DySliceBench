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
ab = []
for i in range(n):
    a,b = inpl()
    ab.append((a-b,a+b,b))
# ab.sort()
ab.sort(key=lambda x:x[1])
res = 1
r = ab[0][1]
for i in range(1,n):
    if ab[i][0] < r:
        continue
    r = ab[i][1]
    res += 1
print(res)
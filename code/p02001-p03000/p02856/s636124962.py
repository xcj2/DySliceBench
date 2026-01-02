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

m = inp()
d = [0] * m
c = [0] * m
res = 0
for i in range(m):
    d[i], c[i] = inpl()
    res += d[i]*c[i]
tmp = 0
if res % 9 == 0:
    tmp -= 1
print(res//9+tmp+sum(c)-1)


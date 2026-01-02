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
p = inpl()
q = inpl()
p = tuple(p)
q = tuple(q)

a = 0
b = 0
for i,num in enumerate(itertools.permutations(range(1,n+1))):
    if p == num:
        a = i+1
    if q == num:
        b = i+1
print(abs(a-b))
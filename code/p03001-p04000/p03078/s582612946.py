from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

x,y,z,k = inpl()
a = inpl()
b = inpl()
c = inpl()
a.sort(reverse = True)
b.sort(reverse = True)
c.sort(reverse = True)
q = [[-(a[0] + b[0] + c[0]), 0, 0, 0]]
heapify(q)
old = set((0,0,0))
for i in range(k):
    k,l,m,n = heappop(q)
    print(-k)
    if l + 1 < x and not (l+1,m,n) in old:
        heappush(q,[-(a[l+1] + b[m] + c[n]), l+1, m, n])
        old.add((l+1,m,n))
    if m + 1 < y and not(l,m+1,n) in old:
        heappush(q,[-(a[l] + b[m+1] + c[n]), l, m+1, n])
        old.add((l,m+1,n))
    if n + 1 < z and not (l,m,n+1)  in old:
        heappush(q,[-(a[l] + b[m] + c[n+1]), l, m, n+1])
        old.add((l,m,n+1))
    # print(q)
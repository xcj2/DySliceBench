from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,c,k = inpl()
t = inpln(n)
t.sort()
u = [(i+k) for i in t]
res = 0
now = 0
while now < n:
    time = u[now]
    for i in range(c):
        if now == n:
            break
        if t[now] <= time:
            now += 1
        else:
            break
    res += 1
print(res)
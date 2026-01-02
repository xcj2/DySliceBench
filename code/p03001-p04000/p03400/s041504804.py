from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
d,x = inpl()
a = inpln(n)
cnt = 0
for i in range(n):
    for j in range(10000):
        tmp = a[i] * j + 1
        if tmp <= d:
            cnt += 1
        else:
            break
print(cnt+x)
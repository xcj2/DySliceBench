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
ab = [0] * n
for i in range(n):
    a,b = inpl()
    ab[i] = (a+b,a,b)
ab.sort(reverse=True)
# print(ab)
x = 0
y = 0
for i,j in enumerate(ab):
    if i%2:
        y += j[2]
    else:
        x += j[1]
print(x-y)

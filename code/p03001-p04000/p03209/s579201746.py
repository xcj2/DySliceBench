from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,x = inpl()
h = [1] * (n+1)
b = [0] * (n+1)
p = [1] * (n+1)
for i in range(1,n+1):
    h[i] = 3 + h[i-1] * 2
    b[i] = 2 + b[i-1] * 2
    p[i] = h[i] - b[i]
# print(h,p)
def sol(n,x):
    if n == 0 :
        return 0 if x <= 0 else 1
    elif x == 1:
        return 0
    elif x <= 1 + h[n-1]:
        return sol(n-1, x-1)
    elif x == 2 + h[n-1]:
        return p[n-1] + 1
    elif x < h[n]:
        return p[n-1] + 1 + sol(n-1, x-(h[n-1]+2))
    else:
        return p[n-1] * 2 + 1
print(sol(n,x))


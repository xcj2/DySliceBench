from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def f(x):
    cnt = 0
    while True:
        if x%2:
            return cnt
        else:
            x //= 2
            cnt += 1
n = inp()
a = inpl()
res = 0
for i in a:
    res += f(i)
print(res)
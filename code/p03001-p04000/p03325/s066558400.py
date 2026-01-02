from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()

def c(x):
    cnt = 0
    while x%2==0:
        cnt += 1
        x //= 2
    return cnt
mi = 0
for i in range(n):
    mi += c(a[i])
print(mi)
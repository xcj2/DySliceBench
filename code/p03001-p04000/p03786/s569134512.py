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
a = sorted(inpl())
b = [0]
for i in a:
    b.append(b[-1]+i)
res = 0
for i in reversed(range(n)):
    if i == n-1: 
        res += 1
        continue
    if (a[i] + b[i])*2 < a[i+1]:
        break
    res += 1
print(res)


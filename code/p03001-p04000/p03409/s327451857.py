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
x = [inpl() for i in range(n)]
y = [inpl() for i in range(n)]
x.sort(reverse=True)
y.sort(key = lambda x: x[1])
res = 0
used = set()
for i in range(n):
    a,b = x[i][0], x[i][1]
    for j in range(n):
        c,d = y[j][0], y[j][1]
        if a<c and b<d and not j in used:
            res += 1
            used.add(j)
            break
print(res)
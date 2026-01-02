from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def error():
    print(-1)
    quit()

n = inp()
a = inpl()
if n == 0 and sum(a) == 1:
    print(1)
    quit()
can = [0] * (n+1); can[0] = 1
b = [0] * (n+1)
res = [0] * (n+1)

if a[0] != 0:
    error()

for i in range(n):
    can[i+1] = can[i]*2 - a[i+1]
    if can[i+1] < 0:
        error()
can[-1] = 0
b[-1] = 0
res[-1] = a[-1]
for i in range(n)[::-1]:
    b[i] = min(res[i+1], can[i])
    res[i] = a[i] + b[i]
print(sum(res))
from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpln(n)
q = deque([])

for i,j in enumerate(a):
  if i == 0:
    q.append(j)
    continue
  c = bisect.bisect_left(q,j)
  if c == 0:
    q.appendleft(j)
  else:
    q[c-1] = j
    
print(len(q))
  

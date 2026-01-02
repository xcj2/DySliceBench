from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def conb(n,r): 
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n = inp()
a = inpl()
c = Counter(a)
res = 0
d = dict()
for key in list(c):
    # print(c[key])
    if c[key] > 1:
        tmp = conb(c[key], 2)
        res += tmp
        d[key] = tmp
    else:
        d[key] = 0
for i,t in enumerate(a):
    if d[t] == 0:
        print(res)
        continue
    now = d[t] * max(0,c[t]-2) // c[t]
    # print(now)
    print(res - d[t] + now)

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
a.sort()
if n%2 == 0:
    res = 0
    for i in range(n//2-1):
        res -= a[i] * 2
        res += a[n-i-1] * 2
    res += a[n//2] - a[n//2-1]
    print(res)
else:
    res_1 = 0
    res_2 = 0
    l = a[:n//2]
    r = a[n//2:]
    res_1 = sum(r)*2 - (r[0] + r[1]) - sum(l)*2 
    
    l = a[:n//2+1]
    r = a[n//2+1:]
    res_2 = sum(r)*2 - sum(l)*2 + l[-1]+l[-2]
    print(max(res_1, res_2))

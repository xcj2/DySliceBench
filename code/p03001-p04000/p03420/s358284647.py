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

n,k = inpl()
res = 0
if k == 0:
    print(n**2)
    quit()
for b in range(k+1,n+1):
    cnt = 0
    cnt += (b-1)-(k-1)
    cnt += (n-(b-1))//b * (b-k)
    cnt += max(0, (n-(b-1))%b-k)
    res += cnt
print(res)
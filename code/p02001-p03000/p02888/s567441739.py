from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N = inp()
LL = inpl()
LL.sort()
ans = 0
for b in range(N):
    bL = LL[b]
    for a in range(b):
        aL = LL[a]
        cLmax = aL+bL
        ans += max(0,bisect.bisect_left(LL,cLmax)-b-1)

print(ans)

from collections import Counter,defaultdict,deque
import sys,bisect,math,itertools,string,queue
from heapq import heappop, heappush
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,k = inpl()
a = inpl()
f = inpl()
a.sort()
f.sort(reverse=True)
l = -1
r = 10**18

def sol(x):
    cnt = 0
    for i in range(n):
        cnt += max(0, a[i] - x//f[i])
    # print(cnt)
    if cnt <= k:
        return True
    else:
        return False

while l + 1 < r:
    mid = (l+r)//2
    if sol(mid):
        r = mid
    else:
        l = mid
    # print(mid)
print(r)




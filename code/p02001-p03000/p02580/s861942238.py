from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

h,w,m = inpl()
yd = []
for i in range(h):
    yd.append([i,0])
xd = []
for i in range(w):
    xd.append([i,0])
se = set()
def ind(i,j):
    return i*w + j
for _ in range(m):
    a,b = inpl()
    yd[a-1][1] += 1
    xd[b-1][1] += 1
    se.add((a-1,b-1))
yd.sort(key = lambda x:x[1], reverse = True)
xd.sort(key = lambda x:x[1], reverse = True)
ymax = yd[0][1]
yl = []
for i,x in yd:
    if x != ymax: break
    yl.append(i)
xmax = xd[0][1]
xl = []
for i,x in xd:
    if x != xmax: break
    xl.append(i)
res = ymax + xmax - 1
# print(yl,xl,res)
for i in yl:
    for j in xl:
        if not (i,j) in se:
            res += 1
            print(res)
            quit()
print(res)
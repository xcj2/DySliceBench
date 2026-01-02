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
xy = [[] for i in range(n)]
for i in range(n):
    for j in range(inp()):
        a,b = inpl()
        xy[i].append([a,b])
# print(xy)
res = 0
for flag in itertools.product([0,1],repeat=n):
    cnt = 0
    theory = [-1]*n #-1:決まってない 0:不明 1:正直
    f = True
    for i,j in enumerate(flag):
        if theory[i] == -1:
            theory[i] = j
        elif theory[i] != j:
            f = False
            break
        if not j:
            continue
        cnt += 1
        for k in xy[i]:
            if theory[k[0]-1] == -1:
                theory[k[0]-1] = k[1]
            elif theory[k[0]-1] != k[1]:
                f = False
                break
        if not f:
            break
    if not f:
        continue
    res = max(res,cnt)
print(res)
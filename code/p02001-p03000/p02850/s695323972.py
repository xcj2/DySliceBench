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
aa = [0] * (n-1)
bb = [0] * (n-1)
g = [[] for i in range(n)]
res = defaultdict(lambda : defaultdict(int))
for i in range(n-1):
    a,b = inpl()
    aa[i] = a-1
    bb[i] = b-1
    g[a-1].append(b-1)
    g[b-1].append(a-1)
def dfs(i,c=-1,p=-1):
    # print('i:{}'.format(i))
    cnt = 1
    for j in g[i]:
        # print(res[j][i])
        if j == p:
            continue
        if cnt == c:
            cnt += 1
        res[i][j] = cnt
        res[j][i] = cnt
        cnt += 1
        dfs(j,res[i][j],i)
dfs(0)
m = 0
for i in g:
    m = max(m, len(i))
print(m)
for i in range(n-1):
    print(res[aa[i]][bb[i]])
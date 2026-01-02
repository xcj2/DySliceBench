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

n,m = inpl()
py = [inpl() for i in range(m)]
p = [[] for i in range(n+5)]
res = defaultdict(lambda : defaultdict(int))
for i,j in enumerate(py):
    p[j[0]].append(j[1])
for k,i in enumerate(p):
    i.sort()
    for j,_ in enumerate(i):
        res[k][i[j]] = j+1
for i in py:
    print('{0}{1}'.format(str(i[0]).zfill(6),str(res[i[0]][i[1]]).zfill(6)))
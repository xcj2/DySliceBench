from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
mo=10**9+7

n,q=MI()
v=[0]*n
c=[0]*n
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=MI()
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

for i in range(q):
    p,x=MI()
    c[p-1]+=x

#print(c)


def bfs(x):
    p=deque()
    p.append(x)
    while p:
        cur=p.popleft()
        v[cur]=1
        for i in g[cur]:
            if v[i]==0:
                p.append(i)
                c[i]+=c[cur]
bfs(0)

print(*c)

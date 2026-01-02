import sys
#import time
#import copy
from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
#import itertools
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)
 
def ri():
    return list(map(int, input().split()))
def rs():
    return list(input().strip())

n,m = ri()
edge=[[] for _ in range(n)]
for i in range(m):
    a, b = ri()
    a+=-1
    b+=-1
    edge[a].append(b)
    edge[b].append(a)

visited=[0]*n
dis = [0]*n
ans=[0]*n
def bfs(now, p=-1):
    q = deque([])
    q.append((now, p, -1))
    while len(q):
        now, p, d = q.popleft()
        dis[now] = d+1
        visited[now]=1
        ans[now]=p+1
        
        for e in edge[now]:
            if visited[e]==1:
                continue
            if e==now:
                continue
            q.append((e, now, dis[now]))
            visited[e]=1
        
        
        
        
bfs(0)
flag=True
for i in range(n):
    if visited[i]==0:
        flag=False
if flag:
    print("Yes")
    for i in range(1,n):
        print(ans[i])
else:
    print("No")
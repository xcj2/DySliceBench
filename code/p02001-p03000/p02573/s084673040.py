# Python template 
from collections import defaultdict 
import sys
import math 

def get_array(): return list(map(int , sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()

sys.setrecursionlimit(10**6) 
g = defaultdict(set)
(n,m) = get_ints()
visited = [0]*n 


def dfs(i,l,par):
    global visited
    visited[i] = True
    l.append(i)
    for j in g[i]:
        if j!=par and not visited[j]:
            dfs(j,l,i)

for i in range(m):
    (u,v) = get_ints()
    g[u-1].add(v-1)
    g[v-1].add(u-1)

ans = 0
for i in range(n):
    if not visited[i]:
        l = []
        dfs(i,l,-1)
        ans = max(ans,len(l))
        
print(ans)

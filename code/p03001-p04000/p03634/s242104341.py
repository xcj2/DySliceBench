def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return input()
import sys
sys.setrecursionlimit(10 ** 6)
n=I()
nl=[[] for i in range(n)]
used=[False for i in range(n)]
for i in range(n-1):
    a,b,c=IL()
    nl[a-1].append([b-1,c])
    nl[b-1].append([a-1,c])
d=[None for i in range(n)]
def dfs(now,pre,dis):
    used[now]=True
    d[now]=dis
    for i in nl[now]:
        if i[0]!=pre and not used[i[0]]:
            dfs(i[0],now,dis+i[1])
    
    return
q,k=IL()
dfs(k-1,-1,0)
for i in range(q):
    x,y=IL()
    print(d[x-1]+d[y-1])
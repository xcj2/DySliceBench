import sys
sys.setrecursionlimit(10**7)

n = int(input())
l=[list(input()) for _ in range(n)]
es = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if l[i][j]=="1":
            es[i].append(j)
colors = [0 for _ in range(n)]

def dfs(v,color):
    colors[v] = color
    for to in es[v]:
        if colors[to] == color:
            return False
        if colors[to] == 0 and not dfs(to, -color):
            return False
    return True

def is_nibu():
    return dfs(0,1)

if not is_nibu():
    print(-1)
    exit()



d = [[float("inf") for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if l[i][j]=="1":
            d[i][j]=1

for i in range(n):
    d[i][i] = 0

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

ans=0
dd=warshall_floyd(d)
for i in range(n):
    ans=max(ans,max(dd[i]))

print(ans+1)

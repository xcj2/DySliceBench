def multival(): return map(int,input().split())
def data(N=1): return [list(map(int,input().split())) for _ in range(N)]
mod = 10**9 + 7
inf = float("inf")


N,M = multival()
nemat = [[0]*N for _ in range(N)]
ans = M
info = []
for _ in range(M):
    a,b = multival()
    a -= 1; b-= 1
    nemat[a][b] = 1
    nemat[b][a] = 1
    info.append([a,b])

def dfs(now,visited):
    visited[now] = True
    if all(visited):
        global ans
        ans -= 1
        return
    for ne in range(N):
        if nemat[now][ne] == 1 and visited[ne] is False:
            dfs(ne,visited)
    
for i,j in info:
    nemat[i][j] = 0
    nemat[j][i] = 0
    dfs(0,[False]*N)
    nemat[i][j] = 1
    nemat[j][i] = 1

print(ans)
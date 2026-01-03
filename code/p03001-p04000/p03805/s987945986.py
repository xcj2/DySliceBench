def multival(): return map(int,input().split())
def data(N=1): return [list(map(int,input().split())) for _ in range(N)]
mod = 10**9 + 7
inf = float("inf")

N,M = multival()
nemat = [[0]*N for _ in range(N)]
ans = 0
for _ in range(M):
    a,b = multival()
    a -= 1; b-= 1
    nemat[a][b] = 1
    nemat[b][a] = 1

def dfs(now=0,visited=[False]*N):
    visited[now] = True
    if all(visited) is True:
        global ans
        ans += 1
    for ne in range(N):
        if nemat[now][ne] == 1 and visited[ne] is False:
            dfs(ne,visited[:])

dfs()
print(ans)
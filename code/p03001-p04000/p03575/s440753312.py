def solve():
    N, M = map(int, input().split())
    g = [[False] * N for i in range(N)]
    bridge = []
    for i in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        bridge.append((a,b))
        g[a][b] = True
        g[b][a] = True
    
    ans = 0
    for a, b in bridge:
        visited = [False] * N
        g[a][b] = False
        g[b][a] = False
        if not dfs(0,g,visited,N):
            ans += 1

        g[a][b] = True
        g[b][a] = True
    
    print(ans)

def dfs(now, g, visited, N):
    visited[now] = True
    if isAllVisited(visited):
        return True
    
    for next in range(N):
        if g[now][next] and not visited[next]:
            if dfs(next, g, visited, N):
                return True
    
    return False

def isAllVisited(visited):
    for v in visited:
        if not v:
            return False
    
    return True

if __name__ == '__main__':
    solve()
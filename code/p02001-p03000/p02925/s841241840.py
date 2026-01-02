def main():
    n = int(input())
    a = [list(map(lambda x: int(x)-1, input().split())) for _ in range(n)]
    id = [[0]*n for _ in range(n)]
    V = 0
    for i in range(n):
        for j in range(n):
            if i<j:
                id[i][j] = V
                V += 1
    def toID(i, j):
        if i<j:
            return id[i][j]
        else:
            return id[j][i]
    
    to = [[] for _ in range(V)]
    for i in range(n):
        for j in range(n-1):
            a[i][j] = toID(i, a[i][j])
        for j in range(n-2):
            to[a[i][j+1]].append(a[i][j])

    dp, visited, calculated = [1] * V, [0] * V, [0] * V

    def dfs(v, dp, visited, calculated):
        if visited[v]:
            if not calculated[v]:
                return -1
            return dp[v]
        visited[v] = 1
        for u in to[v]:
            res = dfs(u, dp, visited, calculated)
            if res == -1:
                return -1
            dp[v] = max(dp[v], res+1)
        calculated[v] = 1
        return dp[v]

    ans = 0
    for v in range(V):
        res = dfs(v, dp, visited, calculated)
        if res == -1:
            print(-1)
            return
        ans = max(ans, res)
    print(ans)
    return

main()

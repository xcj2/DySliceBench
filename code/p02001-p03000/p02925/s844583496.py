import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
 
MAXN = 1005
MAXV = MAXN*(MAXN-1)//2
 
to = [[] for _ in range(MAXV)]
id = [[[] for _ in range(MAXN)] for _ in range(MAXN)]
 
def toId(i, j):
    if i > j:
        i, j = j, i
    return id[i][j]
visited = [False] * MAXV
calculated = [False] * MAXV
dp = [1] * MAXV
 
def dfs(v):
    if visited[v]:
        if not calculated[v]:
            return -1
        return dp[v]
    visited[v] = True
    dp[v] = 1
 
    for u in to[v]:
        res = dfs(u)
        if res == -1: return -1
        dp[v] = max(dp[v], res+1)
    calculated[v] = True
    return dp[v]
 
def main():
    n = int(input())
    a = [[int(i) for i in readline().split()] for _ in range(n)]
    
    for i in range(n):
        for j in range(n-1):
            a[i][j] -= 1
    V = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                id[i][j] = V
                V += 1
    
    for i in range(n):
        for j in range(n-1):
            a[i][j] = toId(i, a[i][j])
        for j in range(n-2):
            to[a[i][j+1]].append(a[i][j])
    
    ans = 0
    
    for i in range(V):
        res = dfs(i)
        if res == -1:
            print('-1')
            return
        ans = max(ans, res)
    print(ans)
    return
  
if __name__ == '__main__':
    main()
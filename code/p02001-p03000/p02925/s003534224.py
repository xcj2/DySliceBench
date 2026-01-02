MAXN = 1005
MAXV = (MAXN * (MAXN - 1)) // 2
to = [[] for _ in range(MAXV)]
ID = [[-1] * MAXN for _ in range(MAXN)]

def toID(i, j):
    if i > j:
        i, j = j, i
    return ID[i][j]

visited = [False] * MAXV
calculated = [False] * MAXV
dp = [0] * MAXV
def dfs(v):
    if visited[v]: #すでに訪れたことがある時
        if not calculated[v]: #計算されたことがない時 = ループがある
            return -1
        return dp[v]
    visited[v] = True
    dp[v] = 1
    for u in to[v]:
        res = dfs(u)
        if res == -1:
            return -1
        dp[v] = max(dp[v], res + 1)
    calculated[v] = True
    return dp[v]

def main():
    N = int(input())
    a = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

    V = 0 #頂点の数
    for i in range(N - 1):
        for j in range(i + 1, N):
            ID[i][j] = V
            V += 1
    
    for i in range(N):
        for j in range(N - 1):
            a[i][j] = toID(i, a[i][j]) #対戦相手で管理していたのを試合番号に変える
        for j in range(N - 2):
            to[a[i][j + 1]].append(a[i][j])
    
    # import numpy as np
    # print (np.array(to))
    # print (np.array(ID))

    ans = 0
    for i in range(V):
        res = dfs(i)
        if res == -1:
            print (-1)
            return 0
        ans = max(ans, res)
    print (ans)
    return 0

if __name__ == '__main__':
    main()
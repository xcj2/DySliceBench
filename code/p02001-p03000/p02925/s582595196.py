import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

MAXN = 1005
MAXV = MAXN*(MAXN-1)//2
to = [[] for _ in range(MAXV)] # 頂点間の辺の情報
id = [[[] for _ in range(MAXN)] for _ in range(MAXN)] # 試合のid=DAGの頂点番号
def toId(i,j): # 選手idから試合idを返す関数
    if i > j: # i,jが逆になっても試合idは同じ
        i,j = j,i
    return id[i][j]

visited = [False]*MAXV
calculated = [False]*MAXV
dp = [1]*MAXV # Vからスタートしたときの最長経路。頂点の個数ベースで経路の長さを数えるので、初期値は1

def dfs(v):
    if visited[v]:
        if not calculated[v]:
            return -1 # 計算が終わっていない頂点を2度訪れるのはループがあるということ
        return dp[v]
    visited[v] = True
    for u in to[v]: # 全ての辺をなめる
        res = dfs(u)
        if res == -1: return -1 # ループがあれば-1を返す
        dp[v] = max(dp[v], res+1)
    calculated[v] = True
    return dp[v]

def main():
    n = int(input())
    a = [[int(i) for i in readline().split()] for _ in range(n)]
    for i in range(n):
        for j in range(n-1):
            a[i][j] -= 1 # 選手idを0始まりに変換
    V = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                id[i][j] = V
                V += 1 # 0から順に各試合にidを割り振る
    for i in range(n):
        for j in range(n-1):
            a[i][j] = toId(i,a[i][j]) # 選手idを試合id(頂点番号)に置き換える
        for j in range(n-2): # 頂点間の依存関係はn-2個
            to[a[i][j+1]].append(a[i][j])
    ans = 0
    for i in range(V):
        res = dfs(i)
        if res == -1:
            print('-1') # ループがあれば-1を返す（問題文の指示）
            return
        ans = max(ans, res)
    print(ans)
    return

if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    V, E = LI()
    con = [[INF]*V for _ in range(V)]
    for _ in range(E):
        std = LI()
        con[std[0]][std[1]] = std[2]

    # dp[S][i]: 集合Sを使ったiで終わるルートの最短コスト
    dp = [[INF]*V for _ in range(2**V)]
    # 0スタートに限定
    dp[1][0] = 0
    visited = [[False]*V for _ in range(2**V)]

    def dfs(S, i):
        if not visited[S][i]:
            if S&1:
                Smi = S & ~(1<<i)
                for j in range(V):
                    if Smi>>j & 1:
                        tmp = dfs(Smi, j) + con[j][i]
                        if dp[S][i] > tmp:
                            dp[S][i] = tmp
            visited[S][i] = True

        return dp[S][i]

    for i in range(V):
        dfs(2**V-1, i)

    ans = min([dp[-1][i]+con[i][0] for i in range(V)])
    print(ans if ans<INF else -1)

if __name__ == '__main__':
    resolve()

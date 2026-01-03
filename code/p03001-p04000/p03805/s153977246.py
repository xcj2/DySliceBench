import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def do_dp(N, Adj):
    univ = 2**(N-1) - 1
    dp = [[0]*(N-1) for i in range(univ + 1)]

    for u in range(N - 1):
        if Adj[0][u+1]:
            dp[1<<u][u] = 1

    for S in range(univ + 1):
        for v in range(N - 1):
            S2 = S & (univ ^ (1 << v))
            for u in range(N):
                if ((1 << u) & S2) and Adj[u+1][v+1]:
                    dp[S][v] += dp[S2][u]

    # debug(dp, locals())
    ans = sum(dp[univ][u] for u in range(N - 1))

    return ans

def solve():
    N, M = map(int, input().split())
    Adj = [[0]*N for i in range(N)]

    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        Adj[a][b] = 1
        Adj[b][a] = 1

    ans = do_dp(N, Adj)

    print(ans)

if __name__ == '__main__':
    solve()
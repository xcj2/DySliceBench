import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

MAXN = 100005
G = [[] for _ in range(MAXN)]
dp = [[] for _ in range(MAXN)]
deg = [0] * MAXN
parents = [-1] * MAXN
result = [0] * MAXN

def dfs1(v,mod,p = -1):
    ans = 1
    for i in range(deg[v]):
        e = G[v][i]
        if e == p:
            parents[v] = i
            continue
        dp[v][i] = dfs1(e,mod,v)
        ans *= dp[v][i] + 1
        ans %= mod
    return ans%mod

def dfs2(v,mod,res_p = 1,p = -1):
    if p != -1:
        dp[v][parents[v]] = res_p
    cuml = [1] * (deg[v] + 1)
    cumr = [1] * (deg[v] + 1)
    for i in range(deg[v]):
        cuml[i + 1] = cuml[i] * (1 + dp[v][i]) % mod
    for i in range(deg[v] - 1,-1,-1):
        cumr[i] = cumr[i + 1] * (1 + dp[v][i]) % mod
    result[v] = cumr[0]
    for i in range(deg[v]):
        e = G[v][i]
        if e == p:
            continue
        dfs2(e,mod,cuml[i] * cumr[i + 1] % mod,v)

def main():
    n,m = map(int,input().split())
    for _ in range(n - 1):
        x,y = map(int,input().split())
        x -= 1
        y -= 1
        G[x].append(y)
        G[y].append(x)
    
    for i in range(n):
        deg[i] = len(G[i])
        dp[i] = [1] * deg[i]
    
    dfs1(0,m)
    dfs2(0,m)
    for i in range(n):
        print(result[i])      

if __name__=='__main__':
    main()

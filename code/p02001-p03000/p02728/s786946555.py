import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self,n):
        fact=[1]*(n+1); invfact=[1]*(n+1)
        for i in range(1,n+1): fact[i]=i*fact[i-1]%MOD
        invfact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1): invfact[i]=invfact[i+1]*(i+1)%MOD
        self.__fact=fact; self.__invfact=invfact

    def inv(self,n):
        assert(n>0)
        return self.__fact[n-1]*self.__invfact[n]%MOD

    def fact(self,n):
        return self.__fact[n]

    def invfact(self,n):
        return self.__invfact[n]

    def comb(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[k]*self.__invfact[n-k]%MOD

    def perm(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[n-k]%MOD

def resolve():
    n = int(input())
    mf = modfact(n)
    E = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int,input().split())
        u -= 1; v -= 1
        E[u].append(v)
        E[v].append(u)

    # dp on Tree
    dp = [1] * n
    size = [1] * n
    stack = [(~0, -1), (0, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            for nv in E[v]:
                if nv == p:
                    continue
                stack.append((~nv, v))
                stack.append((nv, v))
        else:
            # v を確定させる
            v = ~v
            for nv in E[v]:
                if nv == p:
                    continue
                size[v] += size[nv]
                dp[v] *= dp[nv] * mf.invfact(size[nv])
                dp[v] %= MOD
            dp[v] *= mf.fact(size[v] - 1)
            dp[v] %= MOD


    def rerooting(v, p):
        if p == -1:
            return

        # dp[p] を v-rooted にする
        dp[p] *= mf.fact(size[p] - size[v] - 1) * mf.invfact(size[p] - 1) * mf.fact(size[v]) * pow(dp[v], MOD-2, MOD)
        dp[p] %= MOD
        size[p] -= size[v]

        # dp[v] を v-rooted にする
        size[v] += size[p]
        dp[v] *= mf.fact(size[v] - 1) * mf.invfact(size[v] - size[p] - 1) * dp[p] * mf.invfact(size[p])
        dp[v] %= MOD

    ans = [None] * n
    stack = [(0, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            rerooting(v, p)
            ans[v] = dp[v]
            for nv in E[v]:
                if nv == p:
                    continue
                stack.append((~nv, v))
                stack.append((nv, v))
        else:
            rerooting(p, ~v)

    print(*ans, sep = '\n')
resolve()
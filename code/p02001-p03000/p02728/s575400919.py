def main():
    import sys
    input = sys.stdin.readline

    # comb init
    mod = 1000000007
    nmax = 2 * 10 ** 5 + 10  # change here
    fac = [0] * nmax
    finv = [0] * nmax
    inv = [0] * nmax
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, nmax):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

    def comb(n, r):
        if n < r:
            return 0
        else:
            return (fac[n] * ((finv[r] * finv[n - r]) % mod)) % mod

    N = int(input())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    """ここから変更"""
    # op: 普通に根を固定した木DPで子の情報を親に集めるときの演算
    def op(a, b):
        return (((a[0] * b[0])%mod * comb(a[1]+b[1]+1, a[1]))%mod, a[1]+b[1]+1)
    ident_op = (1, -1)

    # cum_merge: 累積opどうしをマージするときの演算
    def cum_merge(a, b):
        return (((a[0] * b[0])%mod * comb(a[1]+b[1], a[1]))%mod, a[1]+b[1])
    # 単位元(cum_merge(ident, x) = x)
    ident_cum_merge = (1, 0)
    """ここまで変更"""

    # root=1でまず普通に木DPをする
    # 並行して各頂点につき、子の値の累積opを左右から求めておく
    # その後根から順番に、親からの寄与を求めていく(from_par)
    def Rerooting(adj):
        N = len(adj) - 1
        st = [1]
        seen = [0] * (N + 1)
        seen[1] = 1
        par = [0] * (N + 1)
        child = [[] for _ in range(N + 1)]
        seq = []
        while st:
            v = st.pop()
            seq.append(v)
            for u in adj[v]:
                if not seen[u]:
                    seen[u] = 1
                    par[u] = v
                    child[v].append(u)
                    st.append(u)
        seq.reverse()
        dp = [ident_op] * (N + 1)
        left = [ident_cum_merge] * (N + 1)
        right = [ident_cum_merge] * (N + 1)
        for v in seq:
            tmp = ident_cum_merge
            for u in child[v]:
                left[u] = tmp
                tmp = op(tmp, dp[u])
            tmp = ident_cum_merge
            for u in reversed(child[v]):
                right[u] = tmp
                tmp = op(tmp, dp[u])
            dp[v] = tmp

        seq.reverse()
        from_par = [ident_op] * (N + 1)
        for v in seq:
            if v == 1:
                continue
            from_par[v] = op(cum_merge(left[v], right[v]), from_par[par[v]])
            dp[v] = op(dp[v], from_par[v])

        return dp

    dp = Rerooting(adj)
    for v in range(1, N+1):
        print(dp[v][0])


if __name__ == '__main__':
    main()

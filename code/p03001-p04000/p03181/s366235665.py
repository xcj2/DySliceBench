def main():
    import sys
    input = sys.stdin.readline

    N, mod = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    """ここから変更"""
    # op: 普通に根を固定した木DPで子の情報を親に集めるときの演算
    def op(a, b):
        return (a * (b + 1))%mod

    # cum_merge: 累積opどうしをマージするときの演算
    def cum_merge(a, b):
        return (a * b)%mod
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
        dp = [1] * (N + 1)
        left = [1] * (N + 1)
        right = [1] * (N + 1)
        for v in seq:
            tmp = 1
            for u in child[v]:
                left[u] = tmp
                tmp = op(tmp, dp[u])
            tmp = 1
            for u in reversed(child[v]):
                right[u] = tmp
                tmp = op(tmp, dp[u])
            dp[v] = tmp

        seq.reverse()
        from_par = [0] * (N + 1)
        for v in seq:
            if v == 1:
                continue
            from_par[v] = op(cum_merge(left[v], right[v]), from_par[par[v]])
            dp[v] = op(dp[v], from_par[v])

        return dp

    dp = Rerooting(adj)
    for i in range(1, N+1):
        print(dp[i])


if __name__ == '__main__':
    main()

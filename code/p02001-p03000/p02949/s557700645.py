import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().strip()


def main():
    N, M, P = map(int, input().split())

    """
    あらかじめ各辺のコイン枚数からP引いておけば、求めるのは単純にコイン枚数の最大値となる。
    すなわちこれは「最長経路問題」に他ならない。
    するとコイン枚数を(-1)倍して「最短経路問題」を求めればよく典型問題に帰着。
        ダイクストラ　　　→　負辺があるのでダメ
        ベルマンフォード　→　O(VE)で解けるので今回はこれ
        ワ―シャルフロイド →　O(V^3)なので間に合わない

    ベルマンフォード復習：
        １．スタートする頂点をsとしてd[s] = 0、その他の頂点はd[v] = \inftyで初期化
        ２．重みwの辺u→vに対してd[v] = min(d[v], d[u] + w)
        ３．この更新を「すべての辺」（E本）に対して行う
        ４．２－３ステップをN（頂点数）回繰り返すと値の更新が（負閉路を除き）収束する
    
    ただし本問では負閉路検出後にそれが1-(負閉路)-Nのように頂点1と頂点Nの間にいることを
    確認する必要がある。
    """

    edges = [] # ベルマンフォードするなら頂点よりも辺が主役なので
    repn = [[] for _ in range(N)]
    reverse_repn = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        repn[a - 1].append(b - 1)
        reverse_repn[b - 1].append(a - 1)
        edges.append((a - 1, b - 1, P - c))

    """
    後々必要なので、頂点0「から」たどり着ける頂点と、
    頂点(N-1)「に」たどり着ける頂点をそれぞれ列挙する
    """

    reachable_from_1 = [0] * N
    reachable_to_N = [0] * N
    ok = [0] * N # 始点と終点の間にいる頂点（ここだけ考慮すれば十分）

    def dfs(v):
        if reachable_from_1[v]:
            return
        reachable_from_1[v] = 1
        for u in repn[v]:
            dfs(u)
    
    def reverse_dfs(v):
        if reachable_to_N[v]:
            return
        reachable_to_N[v] = 1
        for u in reverse_repn[v]:
            reverse_dfs(u)
    
    dfs(0)
    reverse_dfs(N - 1)
    for i in range(N):
        if reachable_from_1[i] and reachable_to_N[i]:
            ok[i] = 1

    """
    ここからベルマンフォード
    """

    d = [float("inf")] * N
    d[0] = 0
    step = 0
    update = True
    while update:
        update = False
        for i in range(M):
            a, b, cost = edges[i]
            if not ok[a]: continue
            if not ok[b]: continue
            new_cost = d[a] + cost
            if new_cost < d[b]:
                update = True
                d[b] = new_cost
        step += 1
        if step > N:
            print(-1)
            return
    print(max(0, -d[N - 1]))


if __name__ == "__main__":
    main()

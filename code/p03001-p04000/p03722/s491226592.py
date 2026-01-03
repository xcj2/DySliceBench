import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, M = map(int, input().split())
    edges = []  # ベルマンフォードするなら頂点よりも辺が主役なので
    repn = [[] for _ in range(N)]
    reverse_repn = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        edges.append((a, b, c))
        repn[a].append(b)
        reverse_repn[b].append(a)
    """
    辺の重みを正負逆転させることで単一始点最短経路問題を解けば良い。
    ベルマンフォードで負閉路を検出したら"inf"を返す。
    ABC137Eを参考にする。
    これも負閉路が1~(N-1)のパス上にあることの確認が必要ですね。。。
    """
    reachable_from_1 = [0] * N
    reachable_from_N = [0] * N
    ok = [0] * N

    def dfs(v):
        if reachable_from_1[v]: return
        reachable_from_1[v] = 1
        for u in repn[v]: dfs(u)

    def reverse_dfs(v):
        if reachable_from_N[v]: return
        reachable_from_N[v] = 1
        for u in reverse_repn[v]: reverse_dfs(u)

    dfs(0)
    reverse_dfs(N - 1)
    for i in range(N):
        if reachable_from_1[i] and reachable_from_N[i]: ok[i] = 1

    # ベルマンフォード
    d = [10**18] * N
    d[0] = 0
    step = 0
    update = True
    while update:
        update = False
        for a, b, c in edges:
            if not ok[a]: continue
            if not ok[b]: continue
            new_cost = d[a] - c
            if new_cost < d[b]:
                update = True
                d[b] = new_cost
        step += 1
        if step > N:
            print("inf")
            return
    print(-d[N - 1])


if __name__ == "__main__":
    main()

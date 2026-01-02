# from scipy.sparse.csgraph import floyd_warshall
INF = 100000000


def make_adj_list(vertex, edge):
    adj_list = []
    dp = []

    # adj_listの初期化と入力
    for i in range(vertex):
        adj_list.append([])
        for j in range(vertex):
            if i == j:
                adj_list[i].append(0)
            else:
                adj_list[i].append(INF)
    for i in range(edge):
        s, t, cost = map(int, input().split())
        adj_list[s][t] = cost

    # dpの初期化
    for i in range(1 << vertex):
        dp.append([])
        for j in range(vertex):
            dp[i].append(-1)

    return adj_list, dp


def cal_min_cost(dp, vertex, edge, d, already, now_v):
    if dp[already][now_v] >= 0:
        # すでに通ったことがある場合
        return dp[already][now_v]

    if already == (1 << vertex) - 1 and now_v == 0:
        # 全ての頂点を通った
        dp[already][now_v] = 0
        return dp[already][now_v]

    res = INF
    for i in range(vertex):
        if not already >> i & 1:
            # 次にiに移動する
            res = min(res, cal_min_cost(dp, vertex, edge, d,
                      already | 1 << i, i) + d[now_v][i])
    dp[already][now_v] = res
    return dp[already][now_v]


def main():
    vertex, edge = map(int, input().split())
    adj_list, dp = make_adj_list(vertex, edge)  # 初期化と入力
    # d = floyd_warshall(adj_list)  # それぞれの頂点からの最小を求める
    d = adj_list
    # for k in range(vertex):
    #     for i in range(vertex):
    #         for j in range(vertex):
    #             d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    # print(d)
    # 最短距離は頂点のどこからはじめても変わらないので0からスタートとする
    min_cost = cal_min_cost(dp, vertex, edge, d, 0, 0)  # 計算
    if min_cost == INF:
        print(-1)
    else:
        print(int(min_cost))


if __name__ == "__main__":
    main()


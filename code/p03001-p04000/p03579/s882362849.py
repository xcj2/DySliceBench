#!/usr/bin/env python3

import sys


# 再帰深度の制限
REC_LIMIT = 100000

# 頂点の色
UNDEF = 0
WHITE = 1
BLACK = -WHITE


# 所与のグラフが二部グラフならば，(True, color[])を返す
# さもなければ，(False, None)を返す
# 参考：『プログラミングコンテストチャレンジブック』（第2版）p.94
def is_bipartite_graph(adj_list):
    n = len(adj_list)  # 頂点数
    color = [UNDEF] * n

    # 頂点をWHITEとBLACKで塗っていく
    def dfs(v, c):
        color[v] = c
        for u in adj_list[v]:
            if color[u] == c:
                # 隣接頂点が同色で塗られていたら不可
                return False
            if color[u] == UNDEF and not dfs(u, -c):
                # 隣接頂点が未彩色なら，反対の色で塗れるか
                return False
        return True  # すべて色を塗れた
    for i in range(n):
        if color[i] == 0:
            # 未彩色なら，WHITEで塗ってみる
            if not dfs(i, WHITE):
                return (False, None)
    return (True, color)


def compute_max_additional_edges(n, m, adj_list):
    is_bi, color = is_bipartite_graph(adj_list)
    if not is_bi:
        # 二部グラフではない場合
        return n * (n - 1) // 2 - m
    else:
        # 二部グラフである場合
        w = sum(c == WHITE for c in color)
        b = sum(c == BLACK for c in color)
        return w * b - m


def main():
    # 最大再帰深度の再設定
    sys.setrecursionlimit(REC_LIMIT)
    # 入力の読み込み
    n, m = (int(x) for x in input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        a, b = (int(x) - 1 for x in input().split())
        adj_list[a].add(b)
        adj_list[b].add(a)
    res = compute_max_additional_edges(n, m, adj_list)
    print(res)


if __name__ == '__main__':
    main()

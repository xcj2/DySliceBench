#!/usr/bin/env pypy3

import array
import collections
import heapq
import itertools


AdjacentVertex = collections.namedtuple("AdjacentVertex", "vertex cost")
Town = collections.namedtuple("Town", "idx x y")
INF = 2 ** 31 - 1
NO_VERTEX = -1


# Prim法で頂点0からの最小全域木を求める
def compute_mst_prim(max_v, adj_list):
    # pred[u]は頂点uの「ひとつ前」の頂点を表す
    pred = [NO_VERTEX for _ in range(max_v)]
    # uとpred[u]を結ぶ辺の重みがkey[u]に入る
    key = [INF for _ in range(max_v)]
    key[0] = 0
    # 二分ヒープを優先度付きキューとして用いる
    pq = [(key[v], v) for v in range(max_v)]
    heapq.heapify(pq)
    # 優先度付きキューに頂点が入っているかを示す配列
    in_pq = array.array("B", (True for _ in range(max_v)))
    while pq:
        _, u = heapq.heappop(pq)
        in_pq[u] = False
        for v, v_cost in adj_list[u]:
            if in_pq[v]:
                weight = v_cost
                if weight < key[v]:
                    pred[v] = u
                    key[v] = weight
                    heapq.heappush(pq, (weight, v))
                    in_pq[v] = True
    return (pred, key)


def solve(n, towns):
    txs = sorted(towns, key=lambda t: t.x)
    tys = sorted(towns, key=lambda t: t.y)
    adj_list = [set() for _ in range(n)]
    g = itertools.chain(zip(txs[:-1], txs[1:]), zip(tys[:-1], tys[1:]))
    for t1, t2 in g:
        cost = min(abs(t1.x - t2.x), abs(t1.y - t2.y))
        adj_list[t1.idx].add(AdjacentVertex(t2.idx, cost))
        adj_list[t2.idx].add(AdjacentVertex(t1.idx, cost))
    (_, key) = compute_mst_prim(n, adj_list)
    return sum(key)


def main():
    n = int(input())
    towns = [Town(idx, *(int(z) for z in input().split())) for idx in range(n)]
    res = solve(n, towns)
    print(res)


if __name__ == '__main__':
    main()

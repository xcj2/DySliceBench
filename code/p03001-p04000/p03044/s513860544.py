import sys
import heapq


def input():
    return sys.stdin.readline().strip()


def dijkstra(start, n_nodes, edge):
    dist = [float("inf")] * n_nodes
    dist[start] = 0
    # 優先度キューの準備
    q = [(dist[start], start)]
    heapq.heapify(q)
    while q:
        # スタートから最も最短距離のものを取り出す
        d, i = heapq.heappop(q)
        # 記録してある情報よりも，取り出した要素に入っている距離情報の方が大きければ
        # 打ち切り．次の要素を取り出す操作に戻る
        if dist[i] < d:
            continue
        # そこから移動できる頂点を探し，最短距離が更新できるものがあれば，
        # 距離を更新して，その頂点への距離と頂点の方法を優先度キューにpush
        for cost, j in edge[i]:
            if dist[j] > dist[i] + cost:
                dist[j] = dist[i] + cost
                heapq.heappush(q, (dist[j], j))
    return dist


def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append([w, v - 1])
        edge[v - 1].append([w, u - 1])
    D = dijkstra(0, N, edge)
    for d in D:
        if d % 2 == 0:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    main()

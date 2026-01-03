import sys
import heapq


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


MOD = 10 ** 9 + 7


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
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        edge[a - 1].append((c, b - 1))
        edge[b - 1].append((c, a - 1))
    Q, K = map(int, input().split())
    D = dijkstra(K - 1, N, edge)
    for _ in range(Q):
        x, y = map(int, input().split())
        print(D[x - 1] + D[y - 1])


if __name__ == "__main__":
    main()

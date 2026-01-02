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


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    edge = [[] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            edge[i].append((C[i][j], j))

    D = [dijkstra(i, 10, edge) for i in range(10)]
    answer = 0
    for _ in range(H):
        A = list(map(int, input().split()))
        for w in range(W):
            if A[w] != -1:
                answer += D[A[w]][1]
    print(answer)


if __name__ == "__main__":
    main()

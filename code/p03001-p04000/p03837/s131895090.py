

def warshall_floyd(d, n):
    # d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def read_input():
    n, m = map(int, input().split())

    edges = []
    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((a - 1, b - 1, c))

    return n, m, edges

def submit():
    n, m, edges = read_input()

    # 全ノード間の最短経路を求める
    d = [[float('inf') for _ in range(n)] for _ in range(n)]

    for edge in edges:
        d[edge[0]][edge[1]] = edge[2]
        d[edge[1]][edge[0]] = edge[2]

    for i in range(n):
        d[i][i] = 0

    d = warshall_floyd(d, n)

    # 各edgeについていずれかの2点間の最短経路に含まれうるか確認する
    edge_inuse = [0 for _ in range(m)]
    for e, edge in enumerate(edges):
        for i in range(n):
            for j in range(n):
                dist1 = d[i][j]
                dist2 = d[i][edge[0]] + edge[2] + d[edge[1]][j]

                if dist1 == dist2:
                    edge_inuse[e] = 1
                    break

            if edge_inuse[e] == 1:
                break

    print(m - sum(edge_inuse))
    return


if __name__ == '__main__':
    submit()

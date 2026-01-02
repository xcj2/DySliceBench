import heapq


def prim(adj):
    INF = 3000
    n = len(adj)
    state, d, p = [False] * n, [INF] * n, [-1] * n
    d[0] = 0
    pq = [(d[0], 0)]
    while pq:
        f, u = heapq.heappop(pq)
        state[u] = True
        if d[u] < f:
            continue
        for v, c in adj[u]:
            if state[v]:
                continue
            if c < d[v]:
                d[v] = c
                p[v] = u
                heapq.heappush(pq, (d[v], v))
    return d


def adj_matrix_to_list(matrix):
    n = len(matrix)
    li = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if matrix[u][v] != -1:
                li[u].append((v, matrix[u][v]))
    return li


def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    adj = adj_matrix_to_list(m)
    print(sum(prim(adj)))


if __name__ == '__main__':
    main()


import heapq

N, M, R = map(int, input().split())
r = list(map(int, input().split()))

INF = 1 << 40
G, dist = [[] for i in range(N)], [[INF for k in range(N)] for j in range(N)]


def dijkstra(s):
    check = [0 for i in range(N)]
    dist[s][s], pq = 0, []
    heapq.heappush(pq, (0, s))

    while len(pq) != 0:
        u = heapq.heappop(pq)
        check[u[1]] = 2

        if dist[s][u[1]] < u[0]:
            continue

        for v in G[u[1]]:
            if dist[s][u[1]] + v[1] < dist[s][v[0]]:
                dist[s][v[0]], check[v[0]] = dist[s][u[1]] + v[1], 1
                heapq.heappush(pq, (dist[s][v[0]], v[0]))


check_dfs, cost_lst = [0 for m in range(R)], []


def dfs(s, cnt, cost):
    if cnt == 0:
        cost_lst.append(cost)
        return

    for i in range(R):
        if check_dfs[i] == 0:
            check_dfs[i] = 1
            dfs(r[i]-1, cnt-1, cost+dist[s][r[i]-1])
            check_dfs[i] = 0


def main():
    for i in range(M):
        a, b, c = map(int, input().split())
        G[a-1].append((b-1, c))
        G[b-1].append((a-1, c))

    for i in range(R):
        dijkstra(r[i]-1)

    for i in range(R):
        check_dfs[i] = 1
        dfs(r[i]-1, R-1, 0)
        check_dfs[i] = 0

    print(min(cost_lst))


if __name__ == '__main__':
    main()

from heapq import heapify, heappop, heappush, heappushpop
INF = 10**6 + 1

class PriorityQueue:
    def __init__(self, heap):
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)


def dijkstra(adj: list, s: int):
    Color = [0] * N
    D = [INF] * N
    P = [None] * N

    D[s] = 0
    P[s] = None
    PQ = PriorityQueue([(0, s)])

    while PQ:
        min_cost, u = PQ.pop()

        Color[u] = 2

        if D[u] < min_cost:
            continue

        for idx_adj_u, w_adj_u in adj[u]:
            if Color[idx_adj_u] != 2:
                if D[u] + w_adj_u < D[idx_adj_u]:
                    D[idx_adj_u] = D[u] + w_adj_u
                    P[idx_adj_u] = u
                    PQ.push((D[idx_adj_u], idx_adj_u))
                    Color[idx_adj_u] = 1
    return D, P

N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    if tmp[1] != 0:
        node = tmp[0]
        for i in range(2, 2 + tmp[1] * 2, 2):
            adj[node].append((tmp[i], tmp[i + 1]))

D, P = dijkstra(adj, 0)

for i in range(N):
    print(i, D[i])


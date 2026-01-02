from heapq import heapify, heappop, heappush, heappushpop


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


def main():

    N, M, s, t = map(int, input().split())
    s, t = s - 1, t - 1
    G = [{} for _ in range(N)]

    for _ in range(M):
        u, v, a, b = map(int, input().split())
        u, v = u - 1, v - 1
        G[u][v] = (a, b)    # (yen, snu)
        G[v][u] = (a, b)

    # Dijkstra
    ans = [0] * N
    # exchange at ith station
    # s to i
    q = PriorityQueue([(0, s)])  # (cost, id)
    vis = [False] * N
    while len(q):
        c, v = q.pop()
        if vis[v] is True:
            continue
        ans[v] = c
        vis[v] = True
        for n in G[v].keys():
            if vis[n] is True:
                continue
            q.push((c + G[v][n][0], n))    # pay by yen
    # i to t
    q = PriorityQueue([(0, t)])  # (cost, id)
    vis = [False] * N
    while len(q):
        c, v = q.pop()
        if vis[v] is True:
            continue
        ans[v] += c
        vis[v] = True
        for n in G[v].keys():
            if vis[n] is True:
                continue
            q.push((c + G[v][n][1], n))    # pay by snu

    # calc ans
    MONEY = pow(10, 15)
    for i in range(1, N):
        if ans[N - i] < ans[N - i - 1]:
            ans[N - i - 1] = ans[N - i]
    print('\n'.join(map(lambda x: str(MONEY - x), ans)))


if __name__ == '__main__':
    main()

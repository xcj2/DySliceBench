import sys
from heapq import heappop, heappush
input = sys.stdin.readline


class Data :
    def __init__():
        pass
    def __init__(self, pos, step, cost):
        self.pos = pos
        self.step = step
        self.cost = cost
    def __lt__(self, right):
        return self.cost < right.cost

def dijkstra(N, S, T, edges):
    inf = 10 ** 9 + 7
    dis = []
    for i in range(N + 1):
        dis.append([inf, inf, inf])

    que = []
    dis[S][0] = 0
    heappush(que, Data(S, 0, 0))
    while (len(que)):
        now_d = heappop(que)
        if dis[now_d.pos][now_d.step] < now_d.cost:
            continue

        for edge in edges[now_d.pos] :
            next_d = Data(edge[0], (now_d.step + 1) % 3, now_d.cost + edge[1])
            if dis[next_d.pos][next_d.step] > next_d.cost:
                dis[next_d.pos][next_d.step] = next_d.cost
                heappush(que, next_d)
    
    if (dis[T][0] == 10 ** 9 + 7):
        return -1
    else :
        return dis[T][0] // 3

N, M = map(int, input().split())
edges = []
for i in range(N+1):
    edges.append([])
for i in range(M):
    u, v = map(int, input().split())
    edges[u].append((v, 1))
S, T = map(int, input().split())
print(dijkstra(N, S, T, edges))
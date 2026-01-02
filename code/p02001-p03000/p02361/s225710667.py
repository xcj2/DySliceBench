# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja

# ダイクストラ
from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, value):
        heappush(self._queue, value)

    def pop(self):
        return heappop(self._queue)

    @property
    def empty(self):
        return not self._queue

    def __len__(self):
        return len(self._queue)

    def __contains__(self, item):
        return item in self._queue


V, E, R = map(int, input().split())
edge = [[] for _ in range(V)]
for _ in range(E):
    f, t, d = map(int, input().split())
    edge[f].append((d, t))

queue = PriorityQueue()
queue.push((0, R))
visited = [float('inf')] * V
visited[R] = 0

while True:
    d, v = queue.pop()
    dist = visited[v]
    for e in edge[v]:
        if (e[0] + dist) < visited[e[1]]:
            visited[e[1]] = e[0] + dist
            queue.push((e[0] + dist, e[1]))

    if queue.empty:
        break
        
for i in visited:
    if i == float('inf'):
        print('INF')
    else:
        print(i)


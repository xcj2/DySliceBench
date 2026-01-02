from heapq import heappush, heappop
import sys


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


v, e = map(int, input().split())
if v == 1:
    print(0)
    sys.exit()
edge = [[] for _ in range(v)]
for _ in range(e):
    s, t, w = map(int, input().split())
    # 無向グラフ
    edge[s].append((w, t))
    edge[t].append((w, s))

V = set()
pq = PriorityQueue()
weight = 0
V.add(0)
for i in edge[0]:
    pq.push(i)

while True:
    nw, nv = pq.pop()
    if nv in V:
        continue
    else:
        weight += nw
        V.add(nv)
        for i in edge[nv]:
            pq.push(i)

    if len(V) == v:
        break

print(weight)



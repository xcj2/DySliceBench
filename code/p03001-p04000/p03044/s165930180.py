from collections import defaultdict
import queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


N = int(input())
g = Graph()
q = queue.Queue()
ans = [-1] * N
ans[0] = 0  # 最初の色はどちらでも良いので 0 とする
q.put(0)

for i in range(N-1):
    src, dst, weight = map(int, input().split())
    src -= 1
    dst -= 1
    g.add_edge(src, dst, weight % 2)
    g.add_edge(dst, src, weight % 2)

while not q.empty():
    v = q.get()
    for i in range(len(g.graph[v])):
        u, w = g.graph[v][i]

        # 来てたならスキップ
        if ans[u] != -1:
            continue

        ans[u] = (ans[v] + w) % 2  # w is 0 or 1
        q.put(u)

for a in ans:
    if a < 0:
        a = 0
    print(a)
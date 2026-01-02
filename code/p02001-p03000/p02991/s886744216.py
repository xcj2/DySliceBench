from collections import deque


class Graph:

  def __init__(self, directed=True):
    self.directed = directed
    self.V = set()
    self.E = {}

  def add_edge(self, u, v, weight: float = 1.):
    self.V.add(u)
    self.V.add(v)

    if u not in self.E: self.E[u] = {}
    self.E[u][v] = weight

    if not self.directed:
      if v not in self.E: self.E[v] = {}
      self.E[v][u] = weight


def bfs(graph: Graph, s):
  V, E = graph.V, graph.E

  visited = set()
  pred = {}
  dist = {}
  for v in graph.V: dist[v] = -1

  if not s in E:
    return pred, dist

  visited.add(s)
  dist[s] = 0
  queue = deque()
  queue.append(s)
  while len(queue) > 0:
    u = queue.popleft()
    for v in E[u]:
      if v not in visited:
        pred[v] = u
        dist[v] = dist[u] + 1
        visited.add(v)
        if v in E: queue.append(v)

  return pred, dist


def main():
  graph = Graph()

  N, M = map(int, input().strip().split())
  for _ in range(M):
    u, v = input().strip().split()
    # graph.add_edge(u, v)
    graph.add_edge(u + '_0', v + '_1')
    graph.add_edge(u + '_1', v + '_2')
    graph.add_edge(u + '_2', v + '_0')

  s, t = input().strip().split()

  pred, dist = bfs(graph, s + '_0')
  # pred, dist = bfs(graph, s)
  key = t + '_0'
  if key in dist:
    distance = dist[key]
    if distance % 3 == 0:
      return (distance // 3)

  return -1


print(main())
import heapq

def dijkstra(graph, node, target):
  INF = float("inf")
  dist = [INF] * node
  dist[target] = 0
  que = [(0, target)]
  while que:
    co, one_node = heapq.heappop(que)
    for next_c, next_n in graph[one_node]:
      dist_candi = dist[one_node] + next_c
      if dist_candi < dist[next_n]:
        dist[next_n] = dist_candi
        heapq.heappush(que, (dist[next_n], next_n))
  return dist


class SetGraph:
  def __init__(self, node_num):
    self.n = node_num
    self.graph = [[] for _ in range(self.n)]

  def add_one_edge(self, start, end, cost):
    self.graph[start].append((cost, end))
    self.graph[end].append((cost, start))

  def get_graph(self):
    return self.graph 
  

n, m = map(int, input().split(" "))
graph_set = SetGraph(n)
for i in range(m):
  a, b, c = map(int, input().split(" "))
  graph_set.add_one_edge(a - 1, b - 1, c)
graph = graph_set.get_graph()

cost = []
for i in range(n):
  temp_cost = dijkstra(graph, n, i)
  cost.append(temp_cost)

result = 0
for i in range(n):
  for c, node in graph[i]:
    if cost[i][node] != c:
      result += 1

print(result // 2)
from collections import deque

n = int(input())
adj = [list(map(int, input().split(' '))) for i in range(n)]

class Node:
  def __init__(self, id, ck):
    self.id = id
    self.ck = ck
    self.depth = -1

  def __str__(self):
    return '{} {}'.format(self.id, self.depth)

class Graph:
  def __init__(self):
    self.map = {}

  def get(self, id):
    return self.map[id]

  def set(self, id, ck):
    self.map[id] = Node(id, ck)

  def bfs(self):
    root = self.get(1)
    root.depth = 0
    queue = deque()
    queue.append(root)
    while(len(queue) > 0):
      node = queue.popleft()
      for id in node.ck:
        target = self.get(id)
        if target.depth != -1: continue
        target.depth = node.depth + 1
        queue.append(target)

  def __str__(self):
    return '\n'.join(map(str, [self.get(i + 1) for i in range(len(self.map))]))

graph = Graph()
for data in adj:
  id = data[0]
  ck = data[2:]
  graph.set(id, ck)

graph.bfs()
print(graph)


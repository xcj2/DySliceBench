class UnionFind:
  def __init__(self, v):
    # number of vertices
    self.v = v
    # parents of each node
    self.parents = [None] * v
    # heights of each node
    self.height = [None] * v

  def init(self):
    for i in range(self.v):
      self.parents[i] = i
      self.height[i] = 0

  def find(self, p):
    # finds the group containing p and return the position of its leader
    if self.parents[p] != p:
      self.parents[p] = self.find(self.parents[p])
    return self.parents[p]

  def union(self, p, q):
    parent_p = self.find(p)
    parent_q = self.find(q)

    if parent_p == parent_q: return

    if self.height[p] > self.height[q]:
      self.parents[q] = parent_p
    elif self.height[p] < self.height[q]:
      self.parents[p] = parent_q
    else:
      self.parents[parent_q] = parent_p
      self.height[p] += self.height[q]

  def same(self, p, q):
    return self.find(p) == self.find(q)

class Edge:
  def __init__(self, f, to, cost):
    self.f = f
    self.to = to
    self.cost = cost

  def __lt__(self, arg):
    return self.cost < arg.cost

n = int(input())
edges = []
for i in range(n):
  input_array = list(map(int, input().split()))
  for k in range(len(input_array)):
    if input_array[k] != -1:
      edges.append(Edge(i, k, input_array[k]))

union_find = UnionFind(n)
union_find.init()
edges.sort()

min_cost = 0
mst = []
while len(mst) < n-1:
  edge = edges.pop(0)
  if union_find.same(edge.f, edge.to) == False:
    min_cost += edge.cost
    union_find.union(edge.f, edge.to)
    mst.append(edge)

print(min_cost)

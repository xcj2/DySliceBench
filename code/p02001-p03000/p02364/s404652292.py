class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.height = [0 for i in range(n)]
    
  def get_root(self, i):
    if self.parent[i] == i:
      return i
    else:
      self.parent[i] = self.get_root(self.parent[i])
      return self.parent[i]
    
  def unite(self, i, j):
    root_i = self.get_root(i)
    root_j = self.get_root(j)
    if root_i != root_j:
      if self.height[root_i] < self.height[root_j]:
        self.parent[root_i] = root_j
      else:
        self.parent[root_j] = root_i
        if self.height[root_i] == self.height[root_j]:
          self.height[root_i] += 1
          
  def is_in_group(self, i, j):
    if self.get_root(i) == self.get_root(j):
      return True
    else:
      return False
    
def kruskal(V, e_list):
  #V := ノードの数
  #e_list := [[始点ノード, 終点ノード, コスト], ...]
  e_cost_sorted = []
  for e in e_list:
    e_cost_sorted.append([e[2], e[0], e[1]])
  e_cost_sorted.sort()
  uf_tree = UnionFind(V)
  cost = 0
  for k in range(len(e_cost_sorted)):
    c = e_cost_sorted[k][0]
    i = e_cost_sorted[k][1]
    j = e_cost_sorted[k][2]
    if not uf_tree.is_in_group(i, j):
      uf_tree.unite(i, j)
      cost += c
  print(cost)
  
V, E = map(int, input().split())
e_list = []
for i in range(E):
  e_list.append(list(map(int, input().split())))
kruskal(V, e_list)

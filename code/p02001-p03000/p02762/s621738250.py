import sys
input = lambda: sys.stdin.readline().rstrip()

#https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * self.n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y: return False
    if self.parents[x] > self.parents[y]:
      x, y = y, x
    self.parents[x] += self.parents[y]
    self.parents[y] = x
        
  def issame(self, x, y):
    return self.find(x) == self.find(y)
  
  def get_node_members(self):
    return [[j for j in range(self.n) if self.issame(i, j)] for i in range(self.n)]
  
  def size(self, x):
    return -self.parents[self.find(x)]

N = list(map(int, input().split()))
parents = [-1] * N[0]
def find(x):
  if parents[x] < 0:
    return x
  else:
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
  x = find(x)
  y = find(y)

  if x == y: return False
  if parents[x] > parents[y]:
    x, y = y, x
  parents[x] += parents[y]
  parents[y] = x
        
def issame(x, y):
  return find(x) == find(y)
  
def size(x):
  return -parents[find(x)]
  

results = [0 for i in range(N[0])]
for i in range(N[1]):
  x, y = list(map(int, input().split()))
  x, y = x - 1, y - 1
  results[x] += 1
  results[y] += 1
  union(x, y)
#print(uf.parents)

for i in range(N[2]):
  x, y = list(map(int, input().split()))
  x, y = x - 1, y - 1
  if issame(x, y):
  	results[x] += 1
  	results[y] += 1
  
#print(node_members, results)

print(" ".join([str(size(i) - results[i] - 1) for i in range(N[0])]))
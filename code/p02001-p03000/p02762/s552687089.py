import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
    
  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    
    if x == y:
      return
    
    if self.parents[x] > self.parents[y]:
      x, y = y, x
    
    self.parents[x] += self.parents[y]
    self.parents[y] = x
  
  #xが属するグループに含まれる要素数(サイズ)を返す
  def size(self, x):
    return -self.parents[self.find(x)]
  
  def same(self, x, y):
    return self.find(x) == self.find(y)
  
  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]
  
  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]
  
  def group_count(self):
    return len(self.roots)
  
  #根と根の下に属する要素のリスト辞書を返す
  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
  n, m, k = map(int, input().split())
  deg = [0]*n
  ans = [0]*n
  uf = UnionFind(n)
  for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    uf.union(a, b)
  
  for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.same(c,d):
      deg[c] += 1
      deg[d] += 1
  
  for i in range(n):
    ans[i] = uf.size(i) - 1 -deg[i]
  
  print(' '.join(map(str, ans)))
  
if __name__ == '__main__':
  main()

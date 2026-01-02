import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))


class UnionFind:
  def __init__(self, size):
    self.size = size
    self.parent = [i for i in range(size)]
    self.size = [1 for _ in range(size)]
    self.height = [1 for _ in range(size)]

  def root(self, i):
    if i != self.parent[i]:
      self.parent[i] = self.root(self.parent[i])
    return self.parent[i]

  def union(self, i, j):
    pi, pj = self.root(i), self.root(j)
    if pi == pj:
      return
    if self.height[pi] < self.height[pj]:
      self.parent[pi] = pj
      self.size[pj] += self.size[pi]
    else:
      self.parent[pj] = pi
      self.size[pi] += self.size[pj]
      if self.height[pi] == self.height[pj]:
        self.height[pi] += 1

  def is_same(self, i, j):
    return self.root(i) == self.root(j)


def main():
  n, q = map(int, input().split())
  uf = UnionFind(n)
  for _ in range(q):
    c, x, y = map(int, input().split())
    if c == 1:
      if uf.is_same(x, y):
        print(1)
      else:
        print(0)
    else:
      uf.union(x, y)


if __name__ == '__main__':
  main()


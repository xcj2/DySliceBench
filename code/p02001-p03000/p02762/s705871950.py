import sys
input = sys.stdin.readline
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
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
def solve():
  n,m,k = (int(i) for i in input().split())
  uff = UnionFind(n)
  ufb = UnionFind(n)
  query = [0]*n
  query2 = [[] for _ in range(n)]
  for i in range(m):
    a,b = (int(i)-1 for i in input().split())
    uff.union(a,b)
    query[a] += 1
    query[b] += 1
    query2[a].append(b)
    query2[b].append(a)
  for i in range(k):
    a,b = (int(i)-1 for i in input().split())
    if uff.same(a,b):
      ufb.union(a,b)
      query2[a].append(b)
      query2[b].append(a)
  for i in range(n):
    print(uff.size(i)-1-len(query2[i]), end=" ")
solve()
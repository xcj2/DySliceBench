class UF_weighed:
    def __init__(self, n):
        self.n = n
        self.par = list(range(n+1))
        self.rank = [0]*(n+1)
        self.size = [1]*(n+1)
        self.diff_w = [0]*(n+1)

    def find(self, x):
        if self.par[x] == x: return x
        p = self.find(self.par[x])
        self.diff_w[x] += self.diff_w[self.par[x]]
        self.par[x] = p
        return self.par[x]

    def weight(self, x):
        self.find(x)
        return self.diff_w[x]

    def diff(self, x, y):
        if not self.same(x, y): return None
        return self.weight(y) - self.weight(x)

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y, w):
        w += self.weight(x) - self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y, w = y, x, -w
        self.par[y] = x
        self.size[x] += self.size[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.diff_w[y] = w
        return True
      
def main():
  n,m = map(int, input().split())
  uf = UF_weighed(n+1)
  for _ in range(m):
    a, b, c = map(int, input().split())
    if uf.same(a, b) and uf.diff(a, b) != c:
      return 'No'
    uf.merge(a, b, c)
  return 'Yes'

print(main())

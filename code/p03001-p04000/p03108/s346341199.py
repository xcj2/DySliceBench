import sys


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] == self.rank[y]:
          self.rank[x] += 1
          self.root[y] = x
          self.size[x] += self.size[y]
        elif self.rank[x] < self.rank[y]:
            self.root[x] = y
            self.size[y] += self.size[x]
        else:
            self.root[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def main():
  input = sys.stdin.readline
  N, M = map(int, input().split())
  total = N * (N-1) // 2
  Bridge = []
  for _ in range(M):
    a, b = map(int, input().split())
    Bridge.append([a, b])
  Bridge = Bridge[::-1]
  
  uf = UnionFind(N)
  ans = [0 for _ in range(M+1)]
  for i in range(M):
    a, b = Bridge[i][0], Bridge[i][1]
    if uf.is_same(a, b):
      ans[i+1] = ans[i]
    else:
      a_root = uf.find(a)
      b_root = uf.find(b)
      a_size = uf.size[a_root]
      b_size = uf.size[b_root]
      
      ans[i+1] = ans[i] + a_size * b_size
      uf.unite(a, b)    

  ans = ans[::-1]
  for i in ans[1:M+1]:
    print(total - i)


if __name__ == '__main__':
  main()

import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

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
  def same(self, x, y):
    return self.find(x) == self.find(y)

def main():
    N = int(readline())

    X = []
    Y = []
    for i in range(N):
        x, y = map(int, readline().split())
        X.append([i,x])
        Y.append([i,y])
    X.sort(key=lambda x:x[1])
    Y.sort(key=lambda x:x[1])

    L = []
    for i in range(N-1):
        u, x1 = X[i]
        v, x2 = X[i+1]
        L.append([u,v,x2-x1])
        u, y1 = Y[i]
        v, y2 = Y[i+1]
        L.append([u,v,y2-y1])
    L.sort(key=lambda x:x[2])

    uf = UnionFind(N)
    ans = 0
    for i in range(2*(N-1)):
        u,v,w = L[i]
        if not uf.same(u,v):
            uf.union(u,v)
            ans += w

    print(ans)

if __name__ == '__main__':
    main()
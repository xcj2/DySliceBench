#https://atcoder.jp/contests/abc065/submissions/5881131
import sys
input = sys.stdin.readline
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

def MST(n, E):
    E = sorted(E, key=lambda x: x[2])
    uf = UnionFind(n)
    ct = 0
    for i,j,cost in E:
      if uf.same_check(i,j):
        continue
      else:
        uf.union(i,j)
        ct += cost
    return ct
  
def solve():
  N = int(input())
  X = []
  append=X.append
  for i in range(N):
    x, y = map(int, input().split())
    append((i, x, y))
 
  F = []
  append = F.append
  Y = sorted(X, key = lambda x: x[1])
  for i in range(len(Y)-1):
    append((Y[i][0], Y[i+1][0], abs(Y[i+1][1]-Y[i][1])))
 
  Y = sorted(X, key = lambda x: x[2])
  for i in range(len(Y)-1):
    append((Y[i][0], Y[i+1][0], abs(Y[i+1][2]-Y[i][2])))
 
  print(MST(N, F))

solve()
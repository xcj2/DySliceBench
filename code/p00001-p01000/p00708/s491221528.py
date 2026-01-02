class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
      
      

T = True
while T:
  n = int(input())
  if n == 0:
    quit()
    
  data = UnionFind(n + 1)
  x = [0] * n
  for i in range(n):
    x[i] = list(map(float, input().split()))
  p = int(n * (n - 1) / 2)
  kumi = [0] * p
  q = 0
  for i in range(n):
    one = x[i]
    for j in range(i + 1, n):
      two = x[j]
      L1 = (one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2 + (one[2] - two[2]) ** 2
      L2 = L1 ** (1 / 2) - (one[3] + two[3])
      L2 = max(L2, 0)
      kumi[q] = [i, j, L2]
      q += 1
  kumi = sorted(kumi, key = lambda x:x[2])
  ans = 0
  for i in range(p):
    x, y, z = kumi[i][0], kumi[i][1], kumi[i][2]
    if not data.same_check(x, y):
      data.union(x, y)
      ans += z
  print('{:.3f}'.format(ans))
    
    
    






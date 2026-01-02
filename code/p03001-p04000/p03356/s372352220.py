class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
 
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
 
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[y] = x
        else:
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
 
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
 
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

def main():
  N, M = map(int, input().split())
  p = list(map(int, input().split()))
  xy = [list(map(int, input().split())) for _ in range(M)]
  U = UnionFind(N+1)
  for x, y in xy:
    U.Unite(x, y)
  ans = 0
  for i in range(1, N+1):
    if U.isSameGroup(i, p[i-1]):
      ans += 1
  print(ans)


if __name__ == "__main__":
  main()
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
  N, K, L = map(int, input().split())
  U_road = UnionFind(N)
  U_train = UnionFind(N)
  for _ in range(K):
    p, q = map(int, input().split())
    U_road.Unite(p, q)
  for _ in range(L):
    r, s = map(int, input().split())
    U_train.Unite(r, s)
  connect_dict = {}
  for i in range(1, N+1):
    x, y = U_road.Find_Root(i), U_train.Find_Root(i)
    if (x, y) in connect_dict:
      connect_dict[(x, y)] += 1
    else:
      connect_dict[(x, y)] = 1
  ans = []
  for i in range(1, N+1):
    x, y = U_road.Find_Root(i), U_train.Find_Root(i)
    ans.append(connect_dict[(x, y)])
  ans = list(map(str, ans))
  print(' '.join(ans))

  

if __name__ == "__main__":
  main()
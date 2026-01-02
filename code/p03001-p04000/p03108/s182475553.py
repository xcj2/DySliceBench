import sys
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

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


def main():
  n,m=map(int,input().split())
  uf=UnionFind(n)
  now=n*(n-1)//2
  g=[]
  ans=[now]
  now=n*(n-1)//2
  for i in range(m):
    a,b=map(int,input().split())
    g.append((a-1,b-1))
  #print(g)
  g=g[::-1]
  for a,b in g:
    now-=uf.size(a)*uf.size(b)*(1-uf.same(a,b))
    ans.append(now)
    uf.union(a,b)
  ans=ans[:-1][::-1]
  print("\n".join(map(str,ans)))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
if __name__ == "__main__":
	main()
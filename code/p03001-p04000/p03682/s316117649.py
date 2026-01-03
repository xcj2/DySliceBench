from operator import itemgetter

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

    def unite(self, x, y):
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
      
n = int(input())
XY = [tuple(map(int, input().split())) for _ in range(n)]
L_to_R = sorted([(xy[0], xy[1], i) for i, xy in enumerate(XY)])
D_to_U = sorted([(xy[0], xy[1], i) for i, xy in enumerate(XY)], key=itemgetter(1))
dist = []
for i in range(n-1):
  x1, y1, num1 = L_to_R[i]
  x2, y2, num2 = L_to_R[i+1]
  d = min(abs(x1-x2), abs(y1-y2))
  dist.append((d, num1, num2))
for i in range(n-1):
  x1, y1, num1 = D_to_U[i]
  x2, y2, num2 = D_to_U[i+1]
  d = min(abs(x1-x2), abs(y1-y2))
  dist.append((d, num1, num2))
dist.sort(reverse=True)  
  
uf = UnionFind(n)
count = 0
ans = 0
while count < n-1:
  d, num1, num2 = dist.pop()
  if uf.same(num1, num2):
    continue
  count += 1
  ans += d
  uf.unite(num1, num2)
print(ans)
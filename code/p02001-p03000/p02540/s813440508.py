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

        
class SegTree:
    
    __slots__ = ["n", "data", "f", "id"]
    
    def __init__(self, li, func, identity):
        self.n = len(li)
        self.f = func
        self.id = identity
        self.data = [self.id]*self.n + li
        for i in range(self.n - 1, 0, -1):
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])
    
    def get(self, i):
        return self.data[i+self.n]
    
    def update(self, i, a):
        i += self.n
        self.data[i] = a
        while i > 1:
            i //= 2
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])
    
    def add(self, i, a):
        i += self.n
        self.data[i] += a
        while i > 1:
            i //= 2
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])
    
    def fold(self, l, r):
        l += self.n
        r += self.n
        res = self.id
        while l < r:
            if l % 2:
                res = self.f(self.data[l], res)
                l += 1
            if r % 2:
                r -= 1
                res = self.f(res, self.data[r])
            l //= 2
            r //= 2
        return res
    
    def max_right(self, l, r, check):
        l += self.n
        r += self.n
        left_li = []
        right_li = []
        while l < r:
            if l % 2:
                left_li.append(l)
                l += 1
            if r % 2:
                r -= 1
                right_li.append(r)
            l //= 2
            r //= 2
        temp = self.id
        for idx in (left_li + right_li[::-1]):
            if not check(self.f(temp, self.data[idx])):
                temp = self.f(temp, self.data[idx])
            else:
                break
        else:
            return -1
        while idx < self.n:
            if check(self.f(temp, self.data[2*idx])):
                idx = 2*idx
            else:
                temp = self.f(temp, self.data[2*idx])
                idx = 2*idx+1
        return idx - self.n
    
    def min_left(self, l, r, check):
        l += self.n
        r += self.n
        left_li = []
        right_li = []
        while l < r:
            if l % 2:
                left_li.append(l)
                l += 1
            if r % 2:
                r -= 1
                right_li.append(r)
            l //= 2
            r //= 2
        temp = self.id
        for idx in (right_li + left_li[::-1]):
            if not check(self.f(self.data[idx], temp)):
                temp = self.f(self.data[idx], temp)
            else:
                break
        else:
            return -1
        while idx < self.n:
            if check(self.f(self.data[2*idx+1], temp)):
                idx = 2*idx+1
            else:
                temp = self.f(temp, self.data[2*idx+1], temp)
                idx = 2*idx
        return idx - self.n


n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]
uf = UnionFind(n)
def f(XY):
  
  Y = [-1]*n
  for i, (x, y) in enumerate(XY):
      Y[x-1] = (i, y)
  seg_max = SegTree([-1]*n, max, -1)
  seg_min = SegTree([n+1]*n, min, n+1)
  idx = dict()
  for x, (i, y) in enumerate(Y):
      t = seg_max.fold(0, y-1)
      if t != -1:
          j = idx[t]
          uf.unite(i, j)
      seg_max.update(y-1, x)
      idx[x] = i
  for x in range(n-1, -1, -1):
      i, y = Y[x]
      t = seg_min.fold(y-1, n)
      if  t != n+1:
          j = idx[t]
          uf.unite(i, j)
      seg_min.update(y-1, x)
        
f(XY)
YX = [(y, x) for x, y in XY]
f(YX)
for i in range(n):
  print(uf.size(i))
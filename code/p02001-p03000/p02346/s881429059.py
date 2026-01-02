# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

def solve():
  N, Q = map(int, input().split())
  ans = []
  bit = BIT(N)
  for i in range(Q):
    com,x,y = map(int, input().split())
    if com==0:
      bit.add(x,y)
    else:
      ans.append(bit.get(x-1,y))
  return ans
print(*solve(),sep='\n')

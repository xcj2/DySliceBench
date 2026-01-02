# Binary Indexed Tree (Fenwick Tree)
class BIT:
  def __init__(self, n):
    self.n = n
    self.bit = [0]*(n+1)
    self.el = [0]*(n+1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.bit[i]
      i -= i & -i
    return s
  def add(self, i, x):
    # assert i > 0
    self.el[i] += x
    while i <= self.n:
      self.bit[i] += x
      i += i & -i
  def get(self, i, j=None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i-1)
  def lower_bound(self,x):
    w = i = 0
    k = 1<<((self.n).bit_length())
    while k:
      if i+k <= self.n and w + self.bit[i+k] < x:
        w += self.bit[i+k]
        i += k
      k >>= 1
    return i+1

def alph_to_num(s):
  return ord(s)-ord('a')

def solve():
  N = int(input())
  S = list(map(alph_to_num,list(input())))
  Q = int(input())
  bits = [BIT(N) for _ in range(26)]
  for i in range(N):
    bits[S[i]].add(i+1,1)
  ans = []
  for _ in range(Q):
    x,y,z = input().split()
    y = int(y)
    if x=='1':
      z = alph_to_num(z)
      bits[S[y-1]].add(y,-1)
      S[y-1] = z
      bits[z].add(y,1)
    if x=='2':
      z = int(z)
      ans.append(sum([bits[i].get(y,z)>0 for i in range(26)]))
  return ans
print(*solve(),sep='\n')
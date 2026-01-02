import sys
input = sys.stdin.readline

import bisect
from collections import defaultdict

AZ = "abcdefghijklmnopqrstuvwxyz"
def DD(arg): return defaultdict(arg)

N = int(input())
words = [w[::-1] for w in list(input().strip() for _ in range(N))]
words.sort()
Lsortwords = sorted([(i,words[i]) for i in range(N)],key = lambda x:-len(x[1]))

class SegmentTree:
  def __init__(self, n, op, e):
    self.n = n
    self.op = op
    self.e = e
    self.size = 2 ** ((n - 1).bit_length())
    self.node = [self.e] * (2 * self.size)
 
  def build(self, array):
    for i in range(self.n):
      self.node[self.size + i] = array[i]
    for i in range(self.size - 1, 0, -1):
      self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])
 
  def update(self, i, val):
    i += self.size
    self.node[i] += val
    while i > 1:
      i >>= 1
      self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])
 
  def get(self, l, r):
    l, r = l + self.size, r + self.size
    res_l, res_r = self.e, self.e
    while l < r:
      if l & 1:
        res_l = self.op(res_l, self.node[l])
        l += 1
      if r & 1:
        r -= 1
        res_r = self.op(self.node[r], res_r) 
      l, r = l >> 1, r >> 1
    return self.op(res_l, res_r)
  
ST = {l:SegmentTree(N,lambda a,b:a+b,0) for l in AZ}
check = [DD(int) for i in range(N)]
ans = 0
shori = 0
for i in range(len(Lsortwords[0][1]))[::-1]:
  for j,w in Lsortwords:
    if len(w) <= i: break
    if not check[j][w[i]]:
      ST[w[i]].update(j,1)
      check[j][w[i]] = 1
  while shori < N and len(Lsortwords[shori][1]) == i+1:
    w = Lsortwords[shori][1]
    p = w[:-1]
    q = w[-1]
    l = bisect.bisect_left(words,p)
    r = bisect.bisect(words,p+chr(97 + 26))
    ans += ST[q].get(l,r)-1
    shori += 1
    if shori == N: break
      
print(ans)
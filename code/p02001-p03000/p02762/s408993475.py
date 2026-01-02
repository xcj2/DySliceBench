N,M,K = list(map(int,input().split()))
import sys
input = sys.stdin.readline
from collections import defaultdict
class UF():
  def __init__(self,n):
    self.n_node = n
    self.l = [i for i in range(n)]
    self.size = [1 for i in range(n)]
    self.d = None
  
  def union(self,i,j):
    if not self.connected(i,j):
      iroot,ipath = self.root(i,return_path=True)
      jroot,jpath = self.root(j,return_path=True)
      if len(jpath) < len(ipath):
        for node in ipath + jpath:
          self.l[node] = iroot
      else:
        for node in ipath + jpath:
          self.l[node] = jroot
        
  def root(self,i,return_path=False):
    path = [i]
    while self.l[i] != i:
      i = self.l[i]
      path.append(self.l[i])
    
    if return_path:
      return i,path
    else:
      return i
  
  def connected(self,i,j):
    if self.root(i) == self.root(j):
      return True
    else:
      return False
  
  def simplify(self):
    for node in range(self.n_node):
      root = self.root(self.l[node])
      if self.l[node] != root:
        self.l[node] = root
  
  def calc_connected(self):
    self.d = defaultdict(set)
    self.simplify()
    for idx,root in enumerate(self.l):
      self.d[root] |= {idx}
    
  def connected_set(self,i):
    if self.d is None:
      self.calc_connected()
    return self.d[self.root(i)]
      
uf = UF(N)
direct_connected = defaultdict(set)
for i in range(M):
  i,j = map(int,input().split())
  i-=1
  j-=1
  
  uf.union(i,j)
  direct_connected[i] |= {j}
  direct_connected[j] |= {i}

block_list = defaultdict(set)
for i in range(K):
  i,j = map(int,input().split())
  i-=1
  j-=1
  if uf.connected(i,j):
    block_list[i] |={j}
    block_list[j] |={i}

  
uf.calc_connected()
for i in range(N):
  print(len(uf.d[uf.l[i]]) - len(direct_connected[i]) - len(block_list[i])-1,end=" ")

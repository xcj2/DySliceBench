# UnionFindでつなげていく
# [所属する木の頂点数]-[1（自分）]-[自分とブロック関係にある人の数]

# UnionFind
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
    
    def show_parents(self):
      print(self.parents)

# ここまでUnionFind
N,M,K=map(int,input().split())

UF=UnionFind(N)
from collections import defaultdict
dic=defaultdict(set)
friends=[0]*N
for i in range(M):
  a,b=map(int,input().split())
  UF.union(a-1,b-1)
  friends[a-1]+=1
  friends[b-1]+=1

for i in range(N):
  dic[UF.find(i)].add(i)

block=defaultdict(set)
for i in range(K):
  c,d=map(int,input().split())
  block[c-1].add(d-1)
  block[d-1].add(c-1)

# UF.show_parents()
# 同じ木に所属する人数のうち、ブロック関係にない人数
ans=[0]*N
for i in range(N):
  candi=dic[UF.find(i)]
  #print("i",candi,"block",block[i])
  ans[i]=len(candi)-friends[i]-1
  for b in block[i]:
    if UF.same(i,b):
      ans[i]-=1
  if ans[i]<0:
    ans[i]=0
print(*ans)

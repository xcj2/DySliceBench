import sys
from collections import defaultdict
class UnionFind():
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]
    def find(self,x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self,x,y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] != self.table[s2]:
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                else:
                    self.table[s1] = s2
            else:
                self.table[s1] += -1
                self.table[s2] = s1
        return
n,k,l = map(int, sys.stdin.readline().split())
p = []
for i in range(k):
    p.append(list(map(int, input().split())))
do = [[] for i in range(n+1)]
for pi in p:  #0-originedに注意
    do[pi[0]].append(pi[1])
p = []
for i in range(l):
    p.append(list(map(int, input().split())))
te = [[] for i in range(n+1)]
for pi in p:  #0-originedに注意
    te[pi[0]].append(pi[1])
dou = UnionFind(n)
for i in range(n+1):
  a = do[i]
  for j in a:
    dou.union(i-1,j-1)
douro = [-1] * n
for i in range(n):
  douro[i] = dou.find(i)
tet = UnionFind(n)
for i in range(n+1):
  a = te[i]
  for j in a:
    tet.union(i-1,j-1)
tetu = [-1] * n
for i in range(n):
  tetu[i] = tet.find(i)
d = defaultdict(int)
for i in range(n): 
  d[(douro[i],tetu[i])] += 1
ans = []
for i in range(n):
  ans.append(d[(douro[i],tetu[i])])
print(" ".join(map(str,ans)))
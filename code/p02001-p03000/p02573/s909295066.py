import sys
import bisect
from functools import lru_cache
from collections import defaultdict
inf = float('inf')
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
class UnionFind():
    def __init__(self, n):
        self.n=n
        self.parents=[-1]*n # 親(uf.find()で経路圧縮して根)の番号。根の場合は-(そのグループの要素数)
    def find(self,x):
        #グループの根を返す
        if self.parents[x]<0:return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    #def members(self, x):
    #    root = self.find(x)
    #    return [i for i in range(self.n) if self.find(i) == root]
    def unite(self,x,y):
        #要素x,yのグループを併合
        x,y=self.find(x),self.find(y)
        if x==y:return
        if self.parents[x]>self.parents[y]:#要素数の大きい方をxに
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x #要素数が大きい方に併合
    def roots(self):
        #全ての根の要素のリスト
        return [i for i, x in enumerate(self.parents) if x<0]
    def group_count(self):
        #グループの数
        return len(self.roots())
    def members(self, x):
        root = self.find(x)
        return len([i for i in range(self.n) if self.find(i) == root])
    #def __str__(self):
    #   return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n,m=reads()
uf=UnionFind(n)
a,b=[0 for i in range(m)],[0 for i in range(m)]
for i in range(m):
    a,b=reads()
    uf.unite(a-1,b-1)
ls=uf.roots()
dic=defaultdict(int)
max=0
y=0
for i in range(n):
    dic[uf.find(i)]+=1
#print(dic)
for num in dic.values():
    if num>max:
        max=num
print(max)
